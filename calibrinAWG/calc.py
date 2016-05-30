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

from db_tables import get_tabla_prop_AWG
from math import sqrt, log10

def alimentacion(sistema):
	if sistema==1:
		k=200
		fac_tri=1
	elif sistema==2:
		k=200
		fac_tri=1
	elif sistema==3:
		k=173
		fac_tri=sqrt(3)
	return k, fac_tri, sistema
		
def corriente_plena_carga(Pot, Volt, FP, efic, sistema):
	tipo_sistema = alimentacion(sistema)
	if tipo_sistema[2]==1:
		Ipc = Pot/(Volt*FP*efic)
	elif tipo_sistema[2]==2:
		Ipc = Pot/(Volt*FP*efic)
	elif tipo_sistema[2]==3:
		Ipc = Pot/(Volt*FP*efic*tipo_sistema[1])
	return Ipc

def corriente_corregida(fa, ft, Ipc):
	Ic = Ipc/(fa*ft)
	return Ic

def corriente_minima(Ipc, Inc=0):
	Imin = Inc + 1.25*Ipc
	return Imin

def seleccion_ampacidad(Ipc, Ic, Imin):
	Inom = max(Ipc, Ic, Imin)
	tabla_AWG = get_tabla_prop_AWG()
	for i in tabla_AWG:
		if Inom <= i[3]:
			Icu = i[3]
			AWG_amp = i[0]
			AWG_z_a = i[1]
			break
	return Icu, AWG_amp, AWG_z_a, Inom

def impedancia_maxima(e_p, Volt, Long, Ipc, k):
	Z_m = (e_p*Volt*1000)/(k*Long*Ipc)
	return Z_m

def impedancia_real(Z_m):
	tabla_AWG = get_tabla_prop_AWG()
	for i in tabla_AWG:
		if Z_m >= i[1]:
			Z_imp = i[1]
			AWG_imp = i[0]
			break
	return Z_imp, AWG_imp

def impedancia_seleccionada(AWG_z_a, Z_imp, AWG_z_cc):
        Z_r = min(AWG_z_a, Z_imp, AWG_z_cc)
        return Z_r

def caida_tension_real(Z_r, k, Ipc, Long, Volt):
	e_r = (Z_r*k*Long*Ipc)/(Volt*1000)
	return e_r

def seccion_conductor_cc(Icc, Tc, Tcc, tcc):
	const_temp = (Tcc+234)/(Tc+234)
	A_cmil = sqrt((tcc*Icc**2)/(0.0297*log10(const_temp)))
	A_mm2 = 0.0005067074791*A_cmil
	tabla_AWG = get_tabla_prop_AWG()
	for i in tabla_AWG:
		if A_mm2 <= i[4]:
			seccion_mm2 = i[4]
			AWG_icc = i[0]
			AWG_z_cc = i[1]
			break
	return seccion_mm2, AWG_icc, AWG_z_cc, A_cmil, A_mm2

#nota: para el calculo de e_real  AWG_amp[2], AWG_imp[0], AWG_icc[2]

def conductor_AWG(AWG_amp, AWG_imp, AWG_icc):
	AWG_f = min(AWG_amp, AWG_imp, AWG_icc)
	tabla_AWG = get_tabla_prop_AWG()
	for i in tabla_AWG:
		if AWG_f == i[1]:
			AWG = i
			AWG_cal = i[0]
			AWG_z = i[1]
			AWG_75 = i[2]
			AWG_90 = i[3]
			AWG_s = i[4]
			AWG_a = i[5]
			
	return AWG_cal, AWG_z, AWG_75, AWG_90, AWG_s, AWG_a, AWG
