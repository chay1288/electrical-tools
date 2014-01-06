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



import calculos

# programa principal

CIR = raw_input('Numero de circuito ')
V = float(input('Voltaje = '))
P = float(input('Potencia = '))
L = float(input('Longitud = '))
fp = float(input('Factor de Potencia = '))
n = float(input('Eficiencia = '))
e = float(input('Caida de tensión deseada = '))
fa = float(input('Factor de agrupamiento = '))
ft = float(input('Factor de temperatura = '))
Tc = float(input('Temperatura del conductor = '))
Tcc = float(input('Temperatura de cortocicuito del conductor = '))
tcc = float(input('Tiempo del cortocircuito = '))
Icc = float(input('Corriente de cortocircuito = '))
sistema = int(input('Tipo de sistema, mono (1), bifasico (2), trifasico (3) ='))


dat = [V, P, L, fp, n, e, fa, ft, Tc, Tcc, tcc, Icc, sistema]

print (' ')

for i in dat:
    print i
    
print (' ')

