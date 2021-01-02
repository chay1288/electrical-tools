#!/usr/bin/python
# -*- coding: utf-8 -*-

# funciones para realizar los calculos.

# Variables utilizadas
#Pot : Potencia
#Volt: Voltaje
#FP  : Factor de potencia
#efic: Eficiencia
#fa  : factor de agrupamiento
#ft  : factor de temperatura
#fr  : factor de resistividad
#fd  : factor de demanda
#Ta  : Temperatura ambiente
#Tc  : Temperatura de operacion del conductor
#Tcc : Temperatura de cortocircuito del conductor
#Icc : Corriente de Cortocircuito
#Ipc : Corriente a plena carga
#Ic  : Corriente corregida con factores
#Imin: Corriente minima
#Inc : Corriente no-continua
#e_p : porcentanje de caida de tension permitida
#Long: Longitud del circuito
#Z_m : Impedencia maxima
#e_r : porcentaje de caida de tension real
#Z_imp: Impedancia del conducto por caida de tension
#Z_r : Impedancia real del calibre del conductor
#tcc : tiempo del cortocircuito

from db_tables import tabla_cal_AWG, tabla_fct, tabla_fca, tabla_itm, tabla_cpt
from math import sqrt, log10

# Seccion de Calculos de Conductores

tabla_AWG = tabla_cal_AWG

# Indice de tabla_cal_AWG
# 0: Calibre
# 1: Impedancia
# 2: Conductor a 60C
# 3: Conductor a 75C
# 4: Conductor a 90C
# 5: Seccion Cobre
# 6: Area, Cobre + Aislante

def alimentacion(sistema):
	if sistema==1:
		K_F=1
		K_E=200
	elif sistema==2:
		K_F=2
		K_E=200
	elif sistema==3:
		K_F=sqrt(3)
		K_E=100*K_F
	return K_E, K_F

def temp_cond(Tc):
	temp = [60,75,90]
	TC = temp.index(Tc)
	return TC

def fct(Ta, TC):
	tabla_FCT = tabla_fct
	for i in tabla_FCT:
		if Ta <= i[0]:
			fct = i
			break
	ft = fct[TC+1]
	return ft

def fca(CTC):
	tablas_FCA = tabla_fca
	for i in tablas_FCA:
		if CTC <= i[0]:
			fa = i[1]
			break
	return fa

def corriente_plena_carga(Pot, Volt, FP, efic, K_F):
	Ipc = Pot/(Volt*FP*efic*K_F)
	return Ipc

def ampacidad_minima(Ipc, TC, Inc=0):
	Imin = Inc + 1.25*Ipc
	global tabla_AWG
	for i in tabla_AWG:
		if Imin <= i[TC+2]:
			amp_min = i[TC+2]
			amp_min_AWG = i[0]
			amp_min_z = i[1]
			break
	return Imin, amp_min_AWG, amp_min, amp_min_z

def ampacidad_corregida(Ipc, fa, ft, TC):
	Ic = Ipc/(fa*ft)
	global tabla_AWG
	for i in tabla_AWG:
		if Ipc <= fa*ft*i[TC+2]:
			amp_c = fa*ft*i[TC+2]
			amp_c_AWG = i[0]
			amp_c_z = i[1]
			break
	return Ic, amp_c_AWG, amp_c, amp_c_z

def conductor_ampacidad(amp_min_z, amp_c_z):
	sel_amp = min(amp_min_z, amp_c_z)
	global tabla_AWG
	for i in tabla_AWG:
		if sel_amp == i[1]:
			AWG_amp = i
			break
	return AWG_amp

def impedancia_maxima_permitida(e_p, Volt, Long, Ipc, K_E):
	Z_max_p = (e_p*Volt*1000)/(K_E*Long*Ipc)
	return Z_max_p

def conductor_impedancia(Z_max_p):
	global tabla_AWG
	for i in tabla_AWG:
		if Z_max_p >= i[1]:
			AWG_imp = i
			break
	return AWG_imp

def seccion_cobre_icc(Icc, Tc, Tcc, tcc):
	const_temp = (Tcc+234)/(Tc+234)
	A_cmil = sqrt((tcc*Icc**2)/(0.0297*log10(const_temp)))
	A_mm2 = 0.0005067074791*A_cmil
	return A_mm2

def conductor_cortocircuito(A_mm2):
	global tabla_AWG
	for i in tabla_AWG:
		if A_mm2 <= i[5]:
			AWG_icc = i
			break
	return AWG_icc

def conductor_AWG(cond_amp, cond_imp, cond_icc):
	AWG_f = min(cond_amp, cond_imp, cond_icc)
	global tabla_AWG
	for i in tabla_AWG:
		if AWG_f == i[1]:
			AWG = i
	return AWG

def caida_tension_real(Z_cond, K_E, Ipc, Long, Volt):
	e_r = (Z_cond*K_E*Long*Ipc)/(Volt*1000)
	return e_r

# Seccion de Calculo de Proteccion de Circuitos
def proteccion_ITM(Ipc, Inc=0):
	I_itm = Inc + 1.25*Ipc
	tabla_ITM = tabla_itm
	for i in tabla_ITM:
		if I_itm <= 1.03*i:
			ITM = i
			break
	return ITM

def conductor_puesta_tierra(ITM):
	tabla_CPT = tabla_cpt
	for i in tabla_CPT:
		if ITM <= i[0]:
			cpt_AWG = i[1]
			break
	global tabla_AWG
	for j in tabla_AWG:
		if cpt_AWG <= j[5]:
			AWG_cpt = j
			break
	return AWG_cpt

# Sección de Calculo de Canalización
