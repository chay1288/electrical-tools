#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------
#
# Name: Cálculo de Calibre de Conductores Eléctricos
# Author: Isaías Hernández
# Date: 19 Enero 2011
# Version: 0.1.0
# Licencia: GPLv3
#
# --------------------------------------------------

import sys
import re
from os import system
from circuits import Circuit

class Menu:
	''' Display menu and respond to choices when run.'''
	def __init__(self):
		self.choices = {
			"1": self.new_circuit,
			"2": self.search_circuit,
			"3": self.list_circuits,
			"4": self.save_current_circuit,
			"5": self.save_all_circuits,
			"6": self.quit
			}

	def display_menu(self):
		system("clear")
		print("""
                  CALIBRAWG v0.1.0
                --------------------

Programa para hacer calculos de calibre de conductor
          en circuitos derivados electricos.


Menu:
	1. Nuevo Circuito Derivado
	2. Buscar Circuito
	3. Lista de Circuitos
	4. Guardar Circuito Actual como .txt
	5. Exportar TODOS los Circuitos como .csv
	6. Salir
			""")

	def run(self):
		"""Display the menu and respond to choices."""
		while True:
			self.display_menu()
			choice = input('Introduzca una opcion del menu: ')
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print('La opcion elegida [',choice,'] no es valida. \nIntente de nuevo.')
				print(' ')
				print(' ')

	def new_circuit(self):
		self.new_circuito = Circuit()
		self.new_circuito.prompt()
		self.new_circuito.compute()
		self.new_circuito.show_results()

	def search_circuit(self):
		id_find = input('\nIntroduzca el ID del Circuito a buscar: ')
		self.new_circuito.search(id_find)

	def list_circuits(self):
		self.new_circuito.list_all_circuits()

	def save_current_circuit(self):
		filename = "REPORTE_"+self.new_circuito.name+".txt"
		with open(filename, "w") as report:
			reporte = self.new_circuito.reporte
			for row in reporte:
				line = ""
				line += row
				line += "\n"
				report.write(line)
			report.close()

	def save_all_circuits(self):
		head_db_reporte = [
			"ID","DATE_TIME","NAME",
			"FASES","VOLT","POT","FP","N","LONG","E","CTC","TA","TC","TCC","CCC","TCC","ICC",
			"K_E","K_F","INDEX_TC","FT","FA",
			"IPC","IMIN","A_MIN_AWG","A_MIN","A_MIN_Z","IC","A_C_AWG","A_C","A_C_Z",
			"AWG_AMP","A_A_Z","A_A_A60C","A_A_A75C","A_A_A90C","A_A_SEC_CU","A_A_AREA",
			"IMP_MAX_PERMITIDA","AWG_IMP","A_Z_Z","A_Z_A60C","A_Z_A75C","A_Z_A90C","A_Z_SEC_CU","A_Z_AREA",
			"SEC_CU_ICC","AWG_ICC","A_I_Z","A_I_A60C","A_I_75C","A_I_90C","A_I_SEC_CU","A_I_AREA",
			"AWG","A_Z,A_A60C","A_A75C","A_90C","A_SEC_CU","A_AREA","E_REAL",
			"ITM","AWG_CPT","A_T_Z","A_T_A60C","A_T_75C","A_T_A90C","A_T_SEC_CU","A_T_AREA"]

		filename = "REPORTE_DB.csv"
		with open(filename, "w") as reportDB:
			db_reporte = self.new_circuito.db_circuits
			for title in head_db_reporte:
				head  = ""
				head += str(title)
				head += ","
				reportDB.write(head)
			reportDB.write("\n")

			for row in db_reporte:
				for item in row:
					line = ""
					line += str(item)
					line += ","
					fila = re.sub(r'[\[\]\(\)]','',line)
					reportDB.write(fila)
				reportDB.write("\n")
			reportDB.close()

	def quit(self):
		print('Gracias por usar CALIBRAWG v0.1.0')
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()
