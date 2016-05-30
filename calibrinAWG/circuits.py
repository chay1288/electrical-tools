#!/usr/bin/python
# -*- coding: utf-8 -*-

import calc
import datetime

last_id = 0

class Circuit:
	"""Creador de datos de circuitos result"""
	db_circuits = []

	def __init__(self, name='Circuito'):
		self.date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id
		self.name = name+str(self.id)
		self.db_circuits.append(self)

	def prompt(self):
		"""Datos proporcionados por el usuario para el calculo"""
		self.v   = float(input(' Voltaje                                    = '))
		self.p   = float(input(' Potencia                                   = '))
		self.l   = float(input(' Longitud                                   = '))
		self.fp  = float(input(' Factor de Potencia                         = '))
		self.n   = float(input(' Eficiencia                                 = '))
		self.e   = float(input(' Caida de tension deseada                   = '))
		self.CTC = float(input(' Conductores en tuberia conduit             = '))
		self.Ta  = float(input(' Temperatura ambiente                       = '))
		self.Tc  = float(input(' Temperatura del conductor                  = '))
		self.Tcc = float(input(' Temperatura de cortocircuito del conductor = '))
		self.ccc = float(input(' Ciclos del cortocircuito                   = '))
		self.tcc = self.ccc/60.0
		self.Icc = float(input(' Corriente de cortocircuito                 = '))
		self.st  = float(input(' Fases                                      = '))

	def compute(self):
		"""Computo de los datos para obtener el calibre del conductor AWG"""
		self.fases = calc.alimentacion(self.st)
		self.TC = calc.temp_cond(self.Tc)
		self.fct = calc.fct(self.Ta, self.Tc)
		self.fca = calc.fca(self.CTC)
		self.ipc = calc.corriente_plena_carga(self.p, self.v, self.fp, self.n, self.st)
		self.ic = calc.corriente_corregida(self.fca, self.fct, self.ipc, self.TC)
		self.imin = calc.corriente_minima(self.ipc, self.TC)
		self.amp = calc.seleccion_ampacidad(self.imin[2], self.ic[2], self.TC)
		self.Zmax = calc.impedancia_maxima(self.e, self.v, self.l, self.ipc, self.fases[0])
		self.Zreal = calc.impedancia_real(self.Zmax)
		self.sicc = calc.seccion_conductor_cc(self.Icc, self.Tc, self.Tcc, self.tcc)
		self.Zsel = calc.impedancia_seleccionada(self.amp[2],self.Zreal[0],self.sicc[2])
		self.ereal = calc.caida_tension_real(self.Zsel, self.fases[0], self.ipc, self.l, self.v)
		self.awg = calc.conductor_AWG(self.amp[2], self.Zreal[0], self.sicc[2])
		self.itm = calc.proteccion_ITM(self.ipc)
		self.cpt = calc.conductor_puesta_tierra(self.itm)

	def show_results(self):
		print(' ')
		print'Fecha: ' ,self.date
		print'ID: ',self.id
		print'Resumen: ',self.name
		print(' ')
		print' Corriente a Plena Carga [Ipc]   = ', self.ipc
		print' Corriente Minima [Imin]         = ', self.imin
		print' Corriente Corregida [Ic]        = ', self.ic
		print' Impedancia Maxima Permitida [Z] = ', self.Zmax
		print(' ')
		print' CALIBRE por Ampacidad    :', self.amp[1], 'AWG'
		print' CALIBRE por Impedancia   :', self.Zreal[1], 'AWG'
		print' CALIBRE por Cortocircuito:', self.sicc[1], 'AWG'
		print(' ')
		print' CALIBRE Seleccionado  ', self.awg[0], 'AWG'
		print' Caida de Tension estimada [e%]  = ', self.ereal
		print(' ')
		print' ITM de proteccion', self.itm, 'A'
		print(' ')
		print' Conductor de Tierra ', self.cpt[0], 'AWG'
	