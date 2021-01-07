#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Implementando la interfaz gráfica (GUI) """

from tkinter import Tk, IntVar, DoubleVar, Frame, Label, Entry, Button,\
    BOTTOM, GROOVE, TOP, LEFT, E
from circuits import Circuit

class CircuitGUI(Circuit, Frame):
    """Crea un circuito para la interfaz gráfica"""

    def __init__(self, master=None):
        Circuit.__init__(self)
        Frame.__init__(self, master)
        self.pack()

        self.fn  = IntVar()
        self.v   = DoubleVar()
        self.p   = DoubleVar()
        self.fp  = DoubleVar()
        self.n   = DoubleVar()

        self.l   = DoubleVar()
        self.e   = DoubleVar()

        self.CTC = IntVar()
        self.Ta  = DoubleVar()

        self.Tc  = DoubleVar()
        self.Tcc = DoubleVar()
        self.ccc = DoubleVar()
        self.Icc = DoubleVar()


        # Valores por defecto
        self.fn.set(1)
        self.v.set(127.0)
        self.fp.set(0.9)
        self.n.set(0.9)
        self.e.set(3.0)
        self.CTC.set(1)
        self.Ta.set(32.0)
        self.Tc.set(90.0)
        self.Tcc.set(105.0)
        self.ccc.set(1.0)
        self.Icc.set(200.0)

    # Declarar variables StringVar, IntVar, DoubleVar, BooleanVar
    def prompt(self):
        """Muestra las etiquetas y las cajas de entrada"""

        self.circuit_window = Frame(self, relief=GROOVE, borderwidth=2)
        self.circuit_window.pack(side=TOP, padx=12, pady=12, anchor="w")

        # Crea etiquetas en Frame de Circuitos y posiciona

        self.fases_label = Label(self.circuit_window, \
                            text="Fases: ")
        self.fases_label.grid(row=0,column=0, sticky=E)

        self.voltaje_label = Label(self.circuit_window, \
                            text="Voltaje: ")
        self.voltaje_label.grid(row=1,column=0, sticky=E)

        self.potencia_label = Label(self.circuit_window, \
                            text="Potencia: ")
        self.potencia_label.grid(row=2,column=0, sticky=E)

        self.factor_potencia_label = Label(self.circuit_window, \
                            text="Factor de Potencia: ")
        self.factor_potencia_label.grid(row=3,column=0, sticky=E)

        self.eficiencia_label = Label(self.circuit_window, \
                            text="Eficiencia: ")
        self.eficiencia_label.grid(row=4,column=0, sticky=E)

        self.longitud_label = Label(self.circuit_window, \
                            text="Longitud: ")
        self.longitud_label.grid(row=5,column=0, sticky=E)

        self.caida_tension_label = Label(self.circuit_window, \
                            text="Caída de Tensión Permitida: ")
        self.caida_tension_label.grid(row=6,column=0, sticky=E)

        self.conductores_conduit_label = Label(self.circuit_window, \
                            text="Conductores en Tubería Conduit: ")
        self.conductores_conduit_label.grid(row=7,column=0, sticky=E)

        self.temperatura_ambiente_label = Label(self.circuit_window, \
                            text="Temperatura Ambiente: ")
        self.temperatura_ambiente_label.grid(row=8,column=0, sticky=E)

        self.temperatura_conductor_label = Label(self.circuit_window, \
                            text="Temperatura de operación de conductor: ")
        self.temperatura_conductor_label.grid(row=9,column=0, sticky=E)

        self.temperatura_cc_label = Label(self.circuit_window, \
                            text="Temperatura de Cortocircuito de conductor: ")
        self.temperatura_cc_label.grid(row=10,column=0, sticky=E)

        self.ciclos_cc_label = Label(self.circuit_window, \
                            text="Ciclos de Cortocircuito: ")
        self.ciclos_cc_label.grid(row=11,column=0, sticky=E)

        self.corriente_cc_label = Label(self.circuit_window, \
                            text="Corriente de Cortocircuito: ")
        self.corriente_cc_label.grid(row=12,column=0, sticky=E)

        # Crea entradas con cajas de texto en Frame de self.circuitos
        self.fases_entry = Entry(self.circuit_window, textvariable=self.fn)
        self.fases_entry.grid(row=0,column=1)

        self.voltaje_entry = Entry(self.circuit_window, textvariable=self.v)
        self.voltaje_entry.grid(row=1,column=1)

        self.potencia_entry = Entry(self.circuit_window, textvariable=self.p)
        self.potencia_entry.grid(row=2,column=1)

        self.factor_potencia_entry = Entry(self.circuit_window, \
                            textvariable=self.fp)
        self.factor_potencia_entry.grid(row=3,column=1)

        self.eficiencia_entry = Entry(self.circuit_window, textvariable=self.n)
        self.eficiencia_entry.grid(row=4,column=1)

        self.longitud_entry = Entry(self.circuit_window, textvariable=self.l)
        self.longitud_entry.grid(row=5,column=1)

        self.caida_tension_entry = Entry(self.circuit_window, \
                            textvariable=self.e)
        self.caida_tension_entry.grid(row=6,column=1)

        self.conductores_conduit_entry = Entry(self.circuit_window, \
                            textvariable=self.CTC)
        self.conductores_conduit_entry.grid(row=7,column=1)

        self.temperatura_ambiente_entry = Entry(self.circuit_window, \
                            textvariable=self.Ta)
        self.temperatura_ambiente_entry.grid(row=8,column=1)

        self.temperatura_conductor_entry = Entry(self.circuit_window, \
                            textvariable=self.Tc)
        self.temperatura_conductor_entry.grid(row=9,column=1)

        self.temperatura_cc_entry = Entry(self.circuit_window, \
                            textvariable=self.Tcc)
        self.temperatura_cc_entry.grid(row=10,column=1)

        self.ciclos_cc_entry = Entry(self.circuit_window, textvariable=self.ccc)
        self.ciclos_cc_entry.grid(row=11,column=1)

        self.corriente_cc_entry = Entry(self.circuit_window, \
                            textvariable=self.Icc)
        self.corriente_cc_entry.grid(row=12,column=1)

    def get_data(self):
        """ Obtener datos de las variables"""

        self.fn  = self.fn.get()
        self.v   = self.v.get()
        self.p   = self.p.get()
        self.fp  = self.fp.get()
        self.n   = self.n.get()

        self.l   = self.l.get()
        self.e   = self.e.get()

        self.CTC = self.CTC.get()
        self.Ta  = self.Ta.get()

        self.Tc  = self.Tc.get()
        self.Tcc = self.Tcc.get()
        self.ccc = self.ccc.get()
        self.tcc = self.ccc/60.0
        self.Icc = self.Icc.get()


        self.data_input = [
            self.fn, self.v, self.p, self.fp, self.n,
            self.l, self.e,
            self.CTC, self.Ta,
            self.Tc, self.Tcc, self.ccc, self.tcc, self.Icc]

        for i in self.db_circuits:
            if self.id is i[0]:
                index_id = self.db_circuits.index(i)
                self.db_circuits[index_id].append(self.data_input)



class MenuGUI(Frame):
    """Ventana Principal del MenuGUI"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.new_circuit()


    def about(self):
        """Información sobre el programa"""

        about_calibrawg = """
CALIBRAWG v0.1.1
----------------

Programa para hacer cálculos de calibre de conductor
en circuitos derivados eléctricos.

"""
        self.about_window = Frame(self, relief=GROOVE, borderwidth=2)
        self.about_window.pack(side=TOP)
        self.about = Label(self, text=about_calibrawg)
        self.about.pack(side=TOP, padx=12, pady=12)

    def new_circuit(self):
        """Frame de Circuitos en Ventana Principal"""
        # objeto de CircuitGUI para aplicar sus metodos en la GUI
        self.circuito_nuevo = CircuitGUI(master=main_window)
        self.circuito_nuevo.prompt()

        # Frame de Botones en Ventana Principal
        self.buttons_windows = Frame(self.circuito_nuevo, \
                            relief=GROOVE, borderwidth=2)
        self.buttons_windows.pack(side=BOTTOM, padx=12, pady=12, anchor="e")

        # Crea botones y posiciona en Frame de Botones
        self.boton_awg = Button(self.buttons_windows, \
                            text="Calcular AWG", bg="#154145", fg="WHITE", \
                            command=self.calcular)
        self.boton_awg.pack(side=LEFT, padx=2, pady=2)

        self.boton_exit = Button(self.buttons_windows, text="Salir", fg="RED",\
                            command=main_window.destroy)
        self.boton_exit.pack(side=LEFT, padx=2, pady=2)

    def calcular(self):
        """Calcula usando circuitos.py"""
        self.circuito_nuevo.get_data()
        self.circuito_nuevo.compute()
        self.circuito_nuevo.show_results()
        self.circuito_nuevo.destroy()
        self.new_circuit()

# Iniciar Ventana Principal, dimensiones y titulo
main_window = Tk()
# main_window.geometry("720x480+0+0")
main_window.title("CalibrAWG v.0.1.1")
# Inicia la instancia de la app
APP = MenuGUI(master=main_window)
# Inicia el loop de la ventana
APP.mainloop()
