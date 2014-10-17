#!/usr/bin/python2
# *-* coding: utf-8 *-*

# INTERFAZ EN NCURSES

#from os import system
import curses 
import calc

class DatosCircuito:
	"""Creador de datos de circuitos cid"""
	def __init__(self):
		wind.addstr( 2,2,'Voltaje                                   = ')
		wind.addstr( 3,2,'Potencia                                  = ')
		wind.addstr( 4,2,'Longitud                                  = ')
		wind.addstr( 5,2,'Factor de Potencia                        = ')
		wind.addstr( 6,2,'Eficiencia                                = ')
		wind.addstr( 7,2,'Caida de tension deseada                  = ')
		wind.addstr( 8,2,'Factor de agrupamiento                    = ')
		wind.addstr( 9,2,'Factor de temperatura                     = ')
		wind.addstr(10,2,'Temperatura del conductor                 = ')
		wind.addstr(11,2,'Temperatura de cortocicuito del conductor = ')
		wind.addstr(12,2,'Ciclos del cortocircuito                  = ')
		wind.addstr(13,2,'Corriente de cortocircuito                = ')
		wind.addstr(14,2,'Fases                                     = ')
		self.v   = float(wind.getstr( 2,48))
		self.p   = float(wind.getstr( 3,48))
		self.l   = float(wind.getstr( 4,48))
		self.fp  = float(wind.getstr( 5,48))
		self.n   = float(wind.getstr( 6,48))
		self.e   = float(wind.getstr( 7,48))
		self.fa  = float(wind.getstr( 8,48))
		self.ft  = float(wind.getstr( 9,48))
		self.Tc  = float(wind.getstr(10,48))
		self.Tcc = float(wind.getstr(11,48))
		self.ccc = float(wind.getstr(12,48))
		self.tcc = self.ccc/60.0
		self.Icc = float(wind.getstr(13,48))
		self.st  = float(wind.getstr(14,48))

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
		self.Zsel = calc.impedancia_seleccionada(self.amp[2],self.Zreal[0],self.sicc[2])
		self.ereal = calc.caida_tension_real(self.Zsel, self.st[0], self.ipc, dat.l, dat.v)
		self.sicc = calc.seccion_conductor_cc(dat.Icc, dat.Tc, dat.Tcc, dat.tcc)
		self.awg = calc.conductor_AWG(self.amp[2], self.Zreal[0], self.sicc[2])



mainscr = curses.initscr()
curses.start_color()
#curses.noecho()
#curses.cbreak()
curses.echo()
mainscr.keypad(1)
mainscr.border(0)
mainscr.addstr( " Calibrin AWG v0.0.5 ", curses.A_BOLD)
mainscr.refresh()


def menu():
	global winm
	mainscr.nodelay(0)
	curses.noecho()
	selection = -1
	option = 0
	while selection < 0:
		graphics = [0]*4
		graphics[option] = curses.A_REVERSE
		dims = mainscr.getmaxyx()
		winm = curses.newwin(3,dims[1],1,0)
		winm.box()
		winm.keypad(1)
		winm.addstr(1,2, "Nuevo Circuito", graphics[0])
		winm.addstr(1,20, "Imprimir", graphics[1])
		winm.addstr(1,32, "Ayuda", graphics[2])
		winm.addstr(1,42, "Salir",graphics[3])
		winm.refresh()
		action = winm.getch()
		if action == curses.KEY_LEFT:
			option = (option - 1) % 4
		elif action == curses.KEY_RIGHT:
			option = (option + 1) % 4
		elif action == ord('\n'):
			selection = option

	if selection == 0:
		datos()
		resultados()
		menu()
	elif selection == 3:
		curses.endwin()

def datos():
	global cid, wind
	curses.echo()
	wind = curses.newwin(18,60,4,2)
	wind.border(0)
	wind.keypad(1)
	wind.addstr(0,27," DATOS ",curses.A_BOLD)
	wind.refresh()
	cid = ResultadoCircuito()
	wind.addstr(16,2,"Presione ENTER ")
	wind.getch()
	wind.clear()


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

menu()

curses.endwin()
