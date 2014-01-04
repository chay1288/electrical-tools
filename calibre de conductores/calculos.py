#! /usr/bin/python
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

import tabla_calibres
from math import sqrt

def alimentacion(sistema):
	if sistema==2:
		k=200
	elif sistema==3:
		k=300
		fac_tri=sqrt(3)
	return k, fac_tri
		
def corriente(Pot, Volt, FP, efic):
	if sistema==2:
		Inom = Pot/(Volt*FP*efic)
	elif sistema==3:
		Inom = Pot/(Volt*FP*efic*alimentacion.fac_tri)

def factos_correccion(fa, ft, fr, fd):
	Icorregida = Pot/(fa*ft*fr*fd)
	return Icorregida
