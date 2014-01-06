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
#Z_r : Impedancia real del calibre del conductor
#tcc : tiempo del cortocircuito

from tabla_calibres import imprimir_tabla
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
	I = [Ipc, Ic, Imin]
	if Ipc > Ic:
		if Ipc > Imin:
			Inom = Ipc
		else:
			Inom = Imin
	elif Ic > Imin:
		Inom = Ic
	else:
		Inom = Imin
	tabla_AWG = imprimir_tabla()
	for i in tabla_AWG:
		if Inom <= i[3]:
			Icu = i[3]
			AWG_amp = i[0]
			AWG_z = i[1]
	return Icu, AWG_amp, AWG_z, Inom, I

def impedancia_maxima(e_p, Volt, Long, Ipc, k):
	Z_m = (e_p*Volt*1000)/(k*Long*Ipc)
	return Z_m

def impedancia_real(Z_m):
	tabla_AWG = imprimir_tabla()
	for i in tabla_AWG:
		if Z_m >= i[1]:
			Z_r = i[1]
			AWG_imp = i[0]
			break
	return Z_r, AWG_imp

def caida_tension_real(Z_r, k, Ipc, Long, Volt):
	e_r = (Z_r*k*Long*Ipc)/(Volt*1000)
	return e_r

def seccion_conductor_cc(Icc, Tc, Tcc, tcc):
	const_temp = (Tcc+234)/(Tc+234)
	A_cmil = sqrt((tcc*Icc**2)/(0.0297*log10(const_temp)))
	A_mm2 = 0.0005067074791*A_cmil
	tabla_AWG = imprimir_tabla()
	for i in tabla_AWG:
		if A_mm <= i[4]:
			seccion_mm2 = i[4]
			AWG_icc = i[0]
			AWG_z = i[1]
			break
	return seccion_mm2, AWG_icc, AWG_z, A_cmil, A_mm2

#nota: para AWG_amp[2], AWG_imp[0], AWG_icc[2]

def conductor_AWG(AWG_amp, AWG_imp, AWG_icc):
	AWG_lista = [AWG_amp, AWG_imp, AWG_icc]
	if AWG_amp < AWG_imp:
		if AWG_amp < AWG_icc:
			AWG_z = AWG_amp
		else:
			AWG_z = AWG_icc
	elif AWG_imp < AWG_icc:
		AWG_z = AWG_imp
	else:
		AWG_z = AWG_icc
	tabla_AWG = imprimir_tabla()
	for i in tabla_AWG:
		if AWG_z == i[1]:
			AWG = i
			AWG_cal = i[0]
			AWG_z = i[1]
			AWG_60 = i[2]
			AWG_75 = i[3]
			AWG_s = i[4]
			AWG_a = i[5]
			
	return AWG_cal, AWG_z, AWG_60, AWG_75, AWG_s, AWG_a, AWG
