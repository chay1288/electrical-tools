#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from os import system
from circuits import Circuit

class Menu:
	''' Display menu and respond to choices when run.'''
	def __init__(self):
		self.choices = {
			"1": self.new_circuit,
			"2": self.quit
			}

	def display_menu(self):
		system("clear")
		print("""
               CALIBRIN AWG v0.0.7
               -------------------

Programa para hacer calculos de calibre de conductor
          en circuitos derivados electricos.


Menu:
	1. Circuito Nuevo
	2. Salir
			""")

	def run(self):
		"""Display the menu and respond to choices."""
		while True:
			self.display_menu()
			choice = raw_input('Introduzca una opcion: ')
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print'La opcion elegida [',choice,'] no es valida. Intente de nuevo.'
				print(' ')
				print(' ')

	def new_circuit(self):
		self.new_circuito = Circuit()
		self.new_circuito.prompt()
		self.new_circuito.compute()
		self.new_circuito.show_results()

	def quit(self):
		print 'Gracias por usar CALIBRIN AWG v0.0.7'
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()	