#! /usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------
#
# Name: Cálculo de Calibre de Conductores Eléctricos
# Author: Isaías Hernández
# Date: 19 Enero 2011
# Version: 0.0.2
# Licencia: GPL
#
# --------------------------------------------------



import math

# programa principal

CIR = raw_input('Numero de circuito ')
V = int(input('Voltaje = '))
P = float(input('Potencia = '))
L = float(input('Longitud = '))
fp = float(input('Factor de Potencia = '))
n = float(input('Eficiencia = '))
e = int(input('Caida de tensión deseada = '))

dat = [V, P, L, fp, e]

print (' ')

for i in dat:
    print i
    
print (' ')

if V==120:
    Inom = P/(V*fp*n)
elif V==127:
    Inom = P/(V*fp*n)
elif V==220:
    bitri = int(input("Escoja alimentacion: bifasica = 2, trifásica = 3 "))
    if bitri==2: 
        Inom = P/(V*fp*n)
    elif bitri==3:
        Inom = P/(V*fp*math.sqrt(3))
elif V==440:
    Inom = P/(V*fp*n*math.sqrt(3))
elif V==460:
    Inom = P/(V*fp*n*math.sqrt(3))
elif V==480:
    Inom = P/(V*fp*n*math.sqrt(3))

print 'Inom = ', Inom, ' A'
print (' ')




def factos():
    fa = float(input('Factor de agrupamiento = '))
    ft = float(input('Factor de temperatura = '))
    fd = float(input('Factor de demanda = '))

    Ic = Inom/(fd*ft*fa)
    print (' ')
    print 'Inom = ', Inom, ' A'
    print (' ')
    print 'Z = ', Z, ' Ohm/km'
    print (' ')
    print ('Ic = ')
    return Ic

if V==120:
    k = 200
elif V==440:
    k = 173
elif V==460:
    k = 173
elif V==480:
    k = 173
else: 
    k = int(input('Introduzca el valor de k '))


Z = (1000*e*V)/(k*Inom*L)

print 'Z = ', Z, ' Ohm/km'
print (' ')
print ('Para introducir los factores de correccion, escriba factos() ')
print (' ')
print ('Introduzca el calibre a utilzar escribiendo "AWG(cal)" ')
print (' ')

def AWG(cal):

    if cal==14:
        Ereal=(8.8582*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==12:
        Ereal=(5.5774*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==10:
        Ereal=(3.6089*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==8:
        Ereal=(2.2965*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==6:
        Ereal=(1.4763*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==4:
        Ereal=(0.9842*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==2:
        Ereal=(0.6561*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==.1:
        Ereal=(0.4265*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==.2:
        Ereal=(0.360892*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==.3:
        Ereal=(0.308398*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==.4:
        Ereal=(0.262467*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==250:
        Ereal=(0.239501*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==300:
        Ereal=(0.213254*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==350:
        Ereal=(0.196859*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==400:
        Ereal=(0.183727*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==500:
        Ereal=(0.164042*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==600:
        Ereal=(0.154199*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==750:
        Ereal=(0.141076*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'
    elif cal==1000:
        Ereal=(0.131233*k*Inom*L)/(V*1000)
        print 'Caida real de voltaje = ', Ereal, ' %'

    print ' '
    print 'Resumen del circuito ', CIR, ':'
    print ' '
    print 'Inom      = ', Inom
    print '%e real   = ', Ereal
    print 'Calibre AWG ', cal
    
    # resumen = ['Inom =', Inom, '%e real = ', Ereal, 'Calibre AWG ', cal]
    # print resumen

# termina programa principal.
