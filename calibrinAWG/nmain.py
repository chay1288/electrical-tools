#!/usr/bin/python2
# *-* coding: utf-8 *-*

# INTERFAZ EN NCURSES

#from os import system
import curses 
import calc

class DatosCircuito:
	"""Creador de datos de circuitos cid"""
	def __init__(self):
		winmenu.addstr( 2,2,'Voltaje                                   = ')
		winmenu.addstr( 3,2,'Potencia                                  = ')
		winmenu.addstr( 4,2,'Longitud                                  = ')
		winmenu.addstr( 5,2,'Factor de Potencia                        = ')
		winmenu.addstr( 6,2,'Eficiencia                                = ')
		winmenu.addstr( 7,2,'Caida de tension deseada                  = ')
		winmenu.addstr( 8,2,'Factor de agrupamiento                    = ')
		winmenu.addstr( 9,2,'Factor de temperatura                     = ')
		winmenu.addstr(10,2,'Temperatura del conductor                 = ')
		winmenu.addstr(11,2,'Temperatura de cortocicuito del conductor = ')
		winmenu.addstr(12,2,'Ciclos del cortocircuito                  = ')
		winmenu.addstr(13,2,'Corriente de cortocircuito                = ')
		winmenu.addstr(14,2,'Fases                                     = ')
		self.v   = float(winmenu.getstr( 2,48))
		self.p   = float(winmenu.getstr( 3,48))
		self.l   = float(winmenu.getstr( 4,48))
		self.fp  = float(winmenu.getstr( 5,48))
		self.n   = float(winmenu.getstr( 6,48))
		self.e   = float(winmenu.getstr( 7,48))
		self.fa  = float(winmenu.getstr( 8,48))
		self.ft  = float(winmenu.getstr( 9,48))
		self.Tc  = float(winmenu.getstr(10,48))
		self.Tcc = float(winmenu.getstr(11,48))
		self.ccc = float(winmenu.getstr(12,48))
		self.tcc = self.ccc/60.0
		self.Icc = float(winmenu.getstr(13,48))
		self.st  = float(winmenu.getstr(14,48))

class ResultadoCircuito:
	"""Resultados. Para obtener el calibre deseado"""	
	def __init__(self):
		dat = DatosCircuito()
		self.st = calc.alimentacion(dat.st)
		self.ipc =calc.corriente_plena_carga(dat.p, dat.v, dat.fp, dat.n, dat.st)
		self.ic = calc.corriente_corregida(dat.fa, dat.ft, self.ipc)
		self.imin = calc.corriente_minima(self.ipc)
		self.amp = calc.seleccion_ampacidad(self.ipc, self.ic, self.imin)
		self.Zmax = calc.impedancia_maxima(dat.e, dat.v, dat.l, self.ipc, self.st[0])
		self.Zreal = calc.impedancia_real(self.Zmax)
		self.ereal = calc.caida_tension_real(self.Zreal[0], self.st[0], self.ipc, dat.l, dat.v)
		self.sicc = calc.seccion_conductor_cc(dat.Icc, dat.Tc, dat.Tcc, dat.tcc)
		self.awg = calc.conductor_AWG(self.amp[2], self.Zreal[0], self.sicc[2])



mainscr = curses.initscr()
curses.start_color()
#curses.noecho()
#curses.cbreak()
curses.echo()
#mainscr.keypad(1)

def menu():
	global winmenu
	winmenu = curses.newwin(6,20,2,2)
	winmenu.border(0)
	winmenu.addstr(0,7," MENU ", curses.A_BOLD)
	winmenu.addstr(2,2, "1 Nuevo Circuito ")
	winmenu.addstr(3,2, "2 Salir ")
	winmenu.addstr(4,2, "Opcion? ")

def datos():
	global cid
	winmenu.clear()
	winmenu.resize(18,60)
	winmenu.redrawwin()
	winmenu.border(0)
	winmenu.addstr(0,27," DATOS ",curses.A_BOLD)
	winmenu.refresh()
	cid = ResultadoCircuito()
	winmenu.addstr(16,2,"Presione ENTER ")
	winmenu.getch()
	winmenu.clear()
def resultados():
	winr = curses.newwin(16,60,20,2)
	winr.border(0)
	winr.addstr(0,24," RESULTADOS ",curses.A_BOLD)
	winr.addstr( 2,2,"Ipc   =")
	winr.addstr( 3,2,"Ic    =")
	winr.addstr( 4,2,"Imin  =")
	winr.addstr( 5,2,"Zmax  =")
	winr.addstr( 6,2,"Acmil =")
	winr.addstr( 7,2,"Amm2  =")
	winr.addstr( 8,2,"e%    =")
	winr.addstr(10,2,"CAL Ampacidad     =")
	winr.addstr(11,2,"CAL Impedancia    =")
	winr.addstr(12,2,"CAL Cortocircuito =")
	winr.addstr(14,2,"CAL SELECCIONADO  =")

	winr.addstr( 2,12,str(cid.ipc ),curses.A_BOLD) 
	winr.addstr( 3,12,str(cid.ic ),curses.A_BOLD) 
	winr.addstr( 4,12,str(cid.imin ),curses.A_BOLD) 
	winr.addstr( 5,12,str(cid.Zmax ),curses.A_BOLD) 
	winr.addstr( 6,12,str(cid.sicc[3] ),curses.A_BOLD) 
	winr.addstr( 7,12,str(cid.sicc[4] ),curses.A_BOLD) 
	winr.addstr( 8,12,str(cid.ereal ),curses.A_BOLD) 
	winr.addstr(10,24,str(cid.amp[1]) + " AWG" ,curses.A_BOLD) 
	winr.addstr(11,24,str(cid.Zreal[1]) + " AWG" ,curses.A_BOLD) 
	winr.addstr(12,24,str(cid.sicc[1]) + " AWG" ,curses.A_BOLD) 
	winr.addstr(14,24,str(cid.awg[0]) + " AWG" ,curses.A_BOLD) 
	
	winr.refresh()
	winr.getch()
new = 0
while new != ord('2'):
	mainscr.clear()
	mainscr.border(0)
	mainscr.addstr( " Calibrin AWG v0.0.4 ", curses.A_BOLD)
	mainscr.refresh()
	menu()
	new = winmenu.getch()
	winmenu.refresh()
	if new == ord('1'):
		datos()	
		resultados()

curses.endwin()
