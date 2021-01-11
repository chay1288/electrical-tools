#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Funciones para la simulación"""

from operator import itemgetter
from calc import caida_tension, tabla_AWG

# Argumentos de caida_tension:
# Z_cond : Impedancia del conductor
# K_E    : Constante de Caida Tension
# Ipc    : Corriente a Plena Carga
# Long   : Longitud del Circuito
# Volt   : Voltaje de la linea


def validar_impedancia(Z_user):
    """Funcion para validar la impedancia dada por usuario con impedancia por
    calibre."""
    global tabla_AWG
    for z in tabla_AWG:
        if Z_user >= z[1]:
            Z_cal = z[0]
            Z_cond = z[1]
            break
    return Z_cal, Z_cond


## Funciones para iterar la caída de tension.

def caida_tension_impedancia(K_E, Ipc, Long, Volt):
    """Simulacion: Impedancia del conductor como parametro."""
    e_results_impedancia = []
    global tabla_AWG
    for z_test in tabla_AWG:
        e_test = caida_tension(z_test[1], K_E, Ipc, Long, Volt)
        e_results_impedancia.append([z_test[0], z_test[1], Ipc, Long, e_test])
    return e_results_impedancia


def caida_tension_longitud(Z_cond, K_E, Ipc, LONG, Volt, STEP):
    """Simulacion: Longitud del conductor como el parametro."""
    LONG_MIN = 1
    LONG_MAX = round(LONG) + STEP
    e_results_longitud = []
    Z_cond = validar_impedancia(Z_cond) #uso individual de impedancias
    for l_test in range(LONG_MIN, LONG_MAX, STEP):
        e_test = caida_tension(Z_cond[1], K_E, Ipc, l_test, Volt)
        e_results_longitud.append([Z_cond[0], Z_cond[1], Ipc, l_test, e_test])
    return e_results_longitud


def caida_tension_corriente(Z_cond, K_E, IPC, Long, Volt, STEP):
    """Simulacion: Corriente del circuito como parametro."""
    IPC_MIN = 1
    IPC_MAX = round(IPC) + STEP
    e_results_corriente = []
    Z_cond = validar_impedancia(Z_cond) #uso individual de impedancias
    for i_test in range(IPC_MIN, IPC_MAX, STEP):
        e_test = caida_tension(Z_cond[1], K_E, i_test, Long, Volt)
        e_results_corriente.append([Z_cond[0], Z_cond[1], i_test, Long, e_test])
    return e_results_corriente

# restriccion de la simulación a un e% estipulado por usuario.
# los datos se ordenan de mayor a menor para una apreciacion de datos.
# los datos son utilizados para graficar con matplotlib.
# si no se cuenta con matplotlib, los datos pueden ser manipulads con 
# otra aplicacion.


def caida_tension_restriccion(e_results_test, e_p):
    e_restriccion = []

    for i in e_results_test:
        while i[4] <= e_p:
            e_restriccion.append(i)
            break

    e_sorted = sorted(e_restriccion, key=itemgetter(4), reverse=True)

    return e_sorted
