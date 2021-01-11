#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Implementando la interfaz gráfica (GUI) para CalibrAWG"""

# --------------------------------------------------
#
# Name: Cálculo de Calibre de Conductores Eléctricos
# Author: Isaías Hernández
# Date: 19 Enero 2011
# Version: 0.2.0
# Licencia: GPLv3
#
# Date: 19 Enero 2021
#
# --------------------------------------------------



import sys
from tkinter import Tk, Menu, Frame, Label, LabelFrame, \
        IntVar, DoubleVar, Entry, Button, \
        TOP, BOTTOM, GROOVE, LEFT, E, W
from circuits import Circuit



class CircuitGUI(Circuit, Frame):
    """Crea una ventana de circuito para la interfaz gráfica"""


    def __init__(self, master=None):
        Circuit.__init__(self)
        Frame.__init__(self, master)
        self.pack()

        # Declarar las variables IntVar(), DoubleVar()
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
        self.l.set(1.0)
        self.e.set(3.0)
        self.CTC.set(1)
        self.Ta.set(32.0)
        self.Tc.set(90.0)
        self.Tcc.set(105.0)
        self.ccc.set(1.0)
        self.Icc.set(200.0)


    def prompt(self):
        """Muestra las etiquetas y las cajas de entrada"""

        self.circuit_labelframe = LabelFrame(self, \
            relief=GROOVE, borderwidth=2, \
            text="Entrada de Datos de Circuito")
        self.circuit_labelframe.pack(padx=12, pady=12, \
            ipadx=12, ipady=12, \
            anchor="center")

        # Crea etiquetas en Frame de Circuitos y posiciona
        Label(self.circuit_labelframe, width=20, anchor=E, \
            text="Fases: ").grid(row=1, column=0)

        Label(self.circuit_labelframe, width=20, anchor=E, \
            text="Voltaje: ").grid(row=2, column=0)

        Label(self.circuit_labelframe, width=20, anchor=E, \
            text="Potencia: ").grid(row=3, column=0)

        Label(self.circuit_labelframe, width=20, anchor=E, \
            text="Factor de Potencia: ").grid(row=4, column=0)

        Label(self.circuit_labelframe, width=20, anchor=E, \
            text="Eficiencia: ").grid(row=5, column=0)

        Label(self.circuit_labelframe, width=25, anchor=E, \
            text="Longitud: ").grid(row=1, column=2)

        Label(self.circuit_labelframe, width=25, anchor=E, \
            text="Caída de Tensión Permitida: ").grid(row=2,column=2)

        Label(self.circuit_labelframe, width=25, anchor=E, \
            text="Conductores en Conduit: ").grid(row=3, column=2)

        Label(self.circuit_labelframe, width=25, anchor=E, \
            text="Temperatura Ambiente: ").grid(row=4, column=2)

        Label(self.circuit_labelframe, width=30, anchor=E,\
            text="Temp. Operación de conductor: ").grid(row=1, column=4)

        Label(self.circuit_labelframe, width=30, anchor=E,\
            text="Temp. Cortocircuito de conductor: ").grid(row=2, column=4)

        Label(self.circuit_labelframe, width=30, anchor=E, \
            text="Ciclos de Cortocircuito: ").grid(row=3, column=4)

        Label(self.circuit_labelframe, width=30, anchor=E, \
            text="Corriente de Cortocircuito: ").grid(row=4, column=4)

        # Crea entradas con cajas de texto en Frame de self.circuitos
        self.fases_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.fn)
        self.fases_entry.grid(row=1,column=1)

        self.voltaje_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.v)
        self.voltaje_entry.grid(row=2,column=1)

        self.potencia_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.p)
        self.potencia_entry.grid(row=3,column=1)

        self.factor_potencia_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.fp)
        self.factor_potencia_entry.grid(row=4,column=1)

        self.eficiencia_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.n)
        self.eficiencia_entry.grid(row=5,column=1)

        self.longitud_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.l)
        self.longitud_entry.grid(row=1,column=3)

        self.caida_tension_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.e)
        self.caida_tension_entry.grid(row=2,column=3)

        self.conductores_conduit_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.CTC)
        self.conductores_conduit_entry.grid(row=3,column=3)

        self.temperatura_ambiente_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.Ta)
        self.temperatura_ambiente_entry.grid(row=4,column=3)

        self.temperatura_conductor_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.Tc)
        self.temperatura_conductor_entry.grid(row=1,column=5)

        self.temperatura_cc_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.Tcc)
        self.temperatura_cc_entry.grid(row=2,column=5)

        self.ciclos_cc_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.ccc)
        self.ciclos_cc_entry.grid(row=3,column=5)

        self.corriente_cc_entry = Entry(self.circuit_labelframe, \
            font="Consolas", width=12, textvariable=self.Icc)
        self.corriente_cc_entry.grid( row=4,column=5)


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

        # Agrupar los datos en la lista
        self.data_input = [
            self.fn, self.v, self.p, self.fp, self.n,
            self.l, self.e,
            self.CTC, self.Ta,
            self.Tc, self.Tcc, self.ccc, self.tcc, self.Icc]

        # Qué hace este bloque?
        for i in self.db_circuits:
            if self.id is i[0]:
                index_id = self.db_circuits.index(i)
                self.db_circuits[index_id].append(self.data_input)



class MenuGUI(Frame):
    """Ventana Principal del MenuGUI para CalibrAWG"""


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="New Circuit", \
            command=self.new_circuit)
        file_menu.add_command(label="Save Current Circuit", \
            command=self.save_current_circuit)
        file_menu.add_command(label="Save ALL Circuits")
        file_menu.add_command(label="Exit", \
            command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu)
        edit_menu.add_command(label="Search Circuit")
        edit_menu.add_command(label="List ALL Circuit")
        menu.add_cascade(label="Edit", menu=edit_menu)

        about_menu = Menu(menu)
        about_menu.add_command(label="About CalibrAWG", \
            command=self.about)
        about_menu.add_command(label="Help!", \
            command=self.help)
        menu.add_cascade(label="About", menu=about_menu)


    def exit_program(self):
        sys.exit()


    def help(self):
        pass


    def about(self):
        """Información sobre el programa"""

        about_calibrawg = """
CALIBRAWG v0.2.0

*Para uso didáctico.* 

Cálculo de calibre de conductores de eléctricos en circuitos derivados de 
acuerdo a tres criterios establecidos en la NOM-001-SEDE-2012 de México. Los
criterios son Ampacidad del conductor, Caída de Tensión en el conductor y 
Corriente de Cortocircuito soportado por el conductor.

El cálculo es para conductores de cobre tipo THW, THHW y THHW-LS con 
temperaturas de 60ºC, 75ºC y 90ºC.

Las unidades en que se realizan los cálculos son con SI (Sistema Internacional)

Python 3.6
19 Enero 2020

Copyright © 2021 Isaías Hernández <chay1288>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

        self.about_window = Tk()
        self.about_window.title("About CalibrAWG")
        self.about_frame = Frame(self.about_window, \
            relief=GROOVE, borderwidth=2)
        self.about_frame.pack(side=TOP, padx=12, pady=12)

        self.about_label = Label(self.about_frame, text=about_calibrawg,\
            anchor=W, justify=LEFT)
        self.about_label.pack(padx=12, pady=12)


    def new_circuit(self):
        """Frame de Circuitos en Ventana Principal"""

        # objeto de CircuitGUI para aplicar sus metodos en la GUI
        self.circuito_nuevo = CircuitGUI(master=main_window)
        self.circuito_nuevo.prompt()

        # Frame de Botones en Ventana Principal
        self.buttons_frame = Frame(self.circuito_nuevo, \
            relief=GROOVE, borderwidth=2)
        self.buttons_frame.pack(side=BOTTOM, padx=12, pady=12, anchor=E)

        # Crea botones y posiciona en Frame de Botones
        self.boton_awg = Button(self.buttons_frame, \
            text="Run", \
            command=self.calcular)
        self.boton_awg.pack(side=LEFT, padx=5, pady=5)

        self.boton_save_current = Button(self.buttons_frame, \
            text="Save", \
            command=self.save_current_circuit)
        self.boton_save_current.pack(side=LEFT, padx=5, pady=5)


    def calcular(self):
        """Calcula usando circuitos.py"""
        self.circuito_nuevo.get_data()
        self.circuito_nuevo.compute()
        self.circuito_nuevo.show_results()
        self.circuito_nuevo.destroy()


    def save_current_circuit(self):
        """Guarda el circuito actual en formato txt"""
        filename = "REPORTE_"+self.circuito_nuevo.name+".txt"
        with open(filename, "w") as report:
            reporte = self.circuito_nuevo.reporte
            for row in reporte:
                line = ""
                line += row
                line += "\n"
                report.write(line)
            report.close()



# Iniciar Ventana Principal, dimensiones y titulo
main_window = Tk()
main_window.geometry("1080x480")
main_window.title("CalibrAWG v.0.1.1")
main_window.resizable(1, 1)

# Inicia la instancia de la app
APP = MenuGUI(master=main_window)
# Inicia el loop de la ventana
APP.mainloop()
