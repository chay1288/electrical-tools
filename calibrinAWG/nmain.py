#!/usr/bin/python2
# *-* coding: utf-8 *-*

# Interfaz en curses

#from os import system
import curses
import calculos

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
		self.st = int(input(' Fases = '))

class ResultadoCircuito:
	"""Resultados. Para obtener el calibre deseado"""	
	def __init__(self):
		dat = DatosCircuito()
		self.st = calculos.alimentacion(dat.st)
		self.ipc = calculos.corriente_plena_carga(dat.p, dat.v, dat.fp, dat.n, dat.st)
		self.ic = calculos.corriente_corregida(dat.fa, dat.ft, self.ipc)
		self.imin = calculos.corriente_minima(self.ipc)
		self.amp = calculos.seleccion_ampacidad(self.ipc, self.ic, self.imin)
		self.Zmax = calculos.impedancia_maxima(dat.e, dat.v, dat.l, self.ipc, self.st[0])
		self.Zreal = calculos.impedancia_real(self.Zmax)
		self.ereal = calculos.caida_tension_real(self.Zreal[0], self.st[0], self.ipc, dat.l, dat.v)
		self.sicc = calculos.seccion_conductor_cc(dat.Icc, dat.Tc, dat.Tcc, dat.tcc)
		self.awg = calculos.conductor_AWG(self.amp[2], self.Zreal[0], self.sicc[2])



mainscr = curses.initscr()
curses.start_color()
#curses.echo()

mainscr.border(0)
mainscr.addstr( " Calibrin AWG v0.0.4 ", curses.A_BOLD)
mainscr.keypad(1)
mainscr.refresh()

new = 0
while new != ord('2'):
	mainscr.refresh()
	winmenu = curses.newwin(6,20,2,2)
	winmenu.border(0)
	winmenu.addstr(0,7," MENU ", curses.A_BOLD)
	winmenu.addstr(2,2, "1 Nuevo Circuito ")
	winmenu.addstr(3,2, "2 Salir ")
	winmenu.addstr(4,2, "Opcion? ")
	new = winmenu.getch()
	winmenu.refresh()
	
	if new == ord('1'):
		winmenu.clear()
		winmenu.resize(15,50)
		winmenu.redrawwin()
		winmenu.border(0)
		winmenu.addstr(0,21," DATOS ",curses.A_BOLD)
		winmenu.refresh()
		winmenu.getch()
		winmenu.clear()


curses.endwin()
