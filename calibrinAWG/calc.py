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
	return K_E, K_F, sistema

def temp_cond(Tc):
	temp = [60,75,90]
	TC = temp.index(Tc)
	return TC

def fct(Ta, Tc):
	tabla_FCT = tabla_fct
	TC = temp_cond(Tc)
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
	
def corriente_plena_carga(Pot, Volt, FP, efic, sistema):
	fases = alimentacion(sistema)
	Ipc = Pot/(Volt*FP*efic*fases[1])
	return Ipc

def corriente_minima(Ipc, TC, Inc=0):
	Imin = Inc + 1.25*Ipc
	global tabla_AWG
	for i in tabla_AWG:
		if Imin <= i[TC+2]:
			Icu_min = i[TC+2]
			AWG_amp_min = i[0]
			AWG_z_a_min = i[1]
			break
	return Icu_min, AWG_amp_min, AWG_z_a_min, Imin 

def corriente_corregida(fa, ft, Ipc, TC):
	Ic = Ipc/(fa*ft)
	global tabla_AWG
	for i in tabla_AWG:
		if Ipc <= fa*ft*i[TC+2]:
			Icu_c = fa*ft*i[TC+2]
			AWG_amp_c = i[0]
			AWG_z_a_c = i[1]
			break
	return Icu_c, AWG_amp_c, AWG_z_a_c, Ic

def seleccion_ampacidad(AWG_z_a_min, AWG_z_a_c, TC):
	sel_amp = min(AWG_z_a_min, AWG_z_a_c)
	global tabla_AWG
	for i in tabla_AWG:
		if sel_amp == i[1]:
			Icu = i[TC+2]
			AWG_amp = i[0]
			AWG_z_a = i[1]
			break
	return Icu, AWG_amp, AWG_z_a

def impedancia_maxima(e_p, Volt, Long, Ipc, K_E):
	Z_m = (e_p*Volt*1000)/(K_E*Long*Ipc)
	return Z_m

def impedancia_real(Z_m):
	global tabla_AWG
	for i in tabla_AWG:
		if Z_m >= i[1]:
			Z_imp = i[1]
			AWG_imp = i[0]
			break
	return Z_imp, AWG_imp

def impedancia_seleccionada(AWG_z_a, Z_imp, AWG_z_cc):
        Z_r = min(AWG_z_a, Z_imp, AWG_z_cc)
        return Z_r

def caida_tension_real(Z_r, K_E, Ipc, Long, Volt):
	e_r = (Z_r*K_E*Long*Ipc)/(Volt*1000)
	return e_r

def seccion_conductor_cc(Icc, Tc, Tcc, tcc):
	const_temp = (Tcc+234)/(Tc+234)
	A_cmil = sqrt((tcc*Icc**2)/(0.0297*log10(const_temp)))
	A_mm2 = 0.0005067074791*A_cmil
	global tabla_AWG
	for i in tabla_AWG:
		if A_mm2 <= i[5]:
			seccion_mm2 = i[5]
			AWG_icc = i[0]
			AWG_z_cc = i[1]
			break
	return seccion_mm2, AWG_icc, AWG_z_cc, A_cmil, A_mm2

#nota: para el calculo de e_real  AWG_amp[2], AWG_imp[0], AWG_icc[2]

def conductor_AWG(AWG_amp, AWG_imp, AWG_icc):
	AWG_f = min(AWG_amp, AWG_imp, AWG_icc)
	global tabla_AWG
	for i in tabla_AWG:
		if AWG_f == i[1]:
			AWG = i
			AWG_cal = i[0]
			AWG_z = i[1]
			AWG_60 = i[2]
			AWG_75 = i[3]
			AWG_90 = i[4]
			AWG_s = i[5]
			AWG_a = i[6]
			
	return AWG_cal, AWG_z, AWG_75, AWG_90, AWG_s, AWG_a, AWG, AWG_60

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
			cpt_AWG = i[2]
			break
	global tabla_AWG
	for j in tabla_AWG:
		if cpt_AWG <= j[0]:
			cpt_area = j[6]
			break
	return cpt_AWG, cpt_area 

# Sección de Calculo de Canalización
