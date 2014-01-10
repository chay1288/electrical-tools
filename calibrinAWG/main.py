#! /usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------
#
# Name: Cálculo de Calibre de Conductores Eléctricos
# Author: Isaías Hernández
# Date: 19 Enero 2011
# Version: 0.0.3
# Licencia: GPLv3
#
# --------------------------------------------------


from os import system
import calc

# programa principal
system("clear")

print(' ')
print('                 CALIBRIN AWG v0.0.3')
print('                 -------------------')
print(' ')
print(' Programa para hacer calculos de calibre de conductor')
print('          en circuitos derivados electricos.')
print(' ')

class DatosCircuito:
	"""Creador de datos de circuitos cid"""
	def __init__(self):
		self.v = float(input(' Voltaje = '))
		self.p = float(input(' Potencia = '))
		self.l = float(input(' Longitud = '))
		self.fp = float(input(' Factor de Potencia = '))
		self.n = float(input(' Eficiencia = '))
		self.e = float(input(' Caida de tensión deseada = '))
		self.fa = float(input(' Factor de agrupamiento = '))
		self.ft = float(input(' Factor de temperatura = '))
		self.Tc = float(input(' Temperatura del conductor = '))
		self.Tcc = float(input(' Temperatura de cortocicuito del conductor = '))
		self.tcc = float(input(' Tiempo del cortocircuito = '))
		self.Icc = float(input(' Corriente de cortocircuito = '))
		self.st = int(input(' Tipo de sistema, mono (1), bifasico (2), trifasico (3) = '))

class ResultadoCircuito:
	
	def __init__(self):
		dat = DatosCircuito()
		self.st = calc.alimentacion(dat.st)
		self.ipc = calc.corriente_plena_carga(dat.p, dat.v, dat.fp, dat.n, dat.st)
		self.ic = calc.corriente_corregida(dat.fa, dat.ft, self.ipc)
		self.imin = calc.corriente_minima(self.ipc)
		self.amp = calc.seleccion_ampacidad(self.ipc, self.ic, self.imin)
		self.Zmax = calc.impedancia_maxima(dat.e, dat.v, dat.l, self.ipc, self.st[0])
		self.Zreal = calc.impedancia_real(self.Zmax)
		self.ereal = calc.caida_tension_real(self.Zreal[0], self.st[0], self.ipc, dat.l, dat.v)
		self.sicc = calc.seccion_conductor_cc(dat.Icc, dat.Tc, dat.Tcc, dat.tcc)
		self.awg = calc.conductor_AWG(self.amp[2], self.Zreal[0], self.sicc[2])


new = 0

while new != 2:
	print(' ')
	print(' Menu')
	print(' ')
	print(' 1 Circuito Nuevo ')
	print(' 2 Salir ')
	print(' ')
	new = input(' Introduzca un numero segun su opcion ')
	system("clear")

	if new == 1:
		print(' ')
		cid = ResultadoCircuito()
		print(' ')
		print('Resultados:')
		print(' ')
		print' Ipc   = ', cid.ipc
		print' Ic    = ', cid.ic
		print' Imin  = ', cid.imin
		print' Zmax  = ', cid.Zmax
		print' Acmil = ', cid.sicc[3]
		print' Amm2  = ', cid.sicc[4]
		print' e%    = ', cid.ereal
		print(' ')
		print' CAL Ampacidad     ', cid.amp[1], 'AWG'
		print' CAL Impedancia    ', cid.Zreal[1], 'AWG'
		print' CAL Cortocircuito ', cid.sicc[1], 'AWG'
		print(' ')
		print' CAL Seleccionado  ', cid.awg[0], 'AWG'
		print(' ')
		print(' ')

