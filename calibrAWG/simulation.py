#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Menu para interactuar con las simulaciones"""

import matplotlib.pyplot as plt
import simulate
from calc import alimentacion


class Simulation:
    """Clase para iniciar una simulacion de caida de tension"""

    def __init__(self):
        pass

    def prompt(self):
        """Datos proporcionados por el usuario para la simulacion"""
        print('=============================================================')
        self.e   = float(input(' Caida de tension limite                = '))
        self.Zt  = float(input(' Impedancia de prueba                   = '))
        self.l   = float(input(' Longitud de prueba                     = '))
        self.v   = float(input(' Voltaje                                = '))
        self.fn  =   int(input(' Fases                                  = '))
        self.Ipc = float(input(' Corriente a plena carga de prueba      = '))
        self.sp  =   int(input(' Incremento de prueba en valores        = '))
        print('=============================================================')


    def compute(self):
        self.ke = alimentacion(self.fn)
        self.zz = simulate.caida_tension_impedancia(self.ke[0], \
                    self.Ipc, self.l, self.v)
        self.zl = simulate.caida_tension_longitud(self.Zt, \
                    self.ke[0], self.Ipc, self.l, self.v, self.sp)
        self.zi = simulate.caida_tension_corriente(self.Zt, \
                    self.ke[0], self.Ipc, self.l, self.v, self.sp)
        self.sz = simulate.caida_tension_restriccion(self.zz, self.e)
        self.sl = simulate.caida_tension_restriccion(self.zl, self.e)
        self.si = simulate.caida_tension_restriccion(self.zi, self.e)


#bloque de prueba

sim = Simulation()
sim.prompt()
sim.compute()


# bloque de graficado con matplotlib

# grafica impedancia vs caida tension
xz = []
yz = []
for xi in sim.sz:
    xz.append(xi[1])
    yz.append(xi[4])

# plt.plot(xz, yz, 'ro--', alpha=0.3, label='Impedancia')
# plt.axis([0,9,0,sim.e])
# plt.xlabel('Z (ohm/km)')
# plt.ylabel('e%')
# plt.title('Impedancia vs Caida de Tension')
# plt.show()

# grafica longitud vs caida de tension

xl = []
yl = []
for xi in sim.sl:
    xl.append(xi[3])
    yl.append(xi[4])

# plt.plot(xl, yl, 'go--', alpha=0.3, label='Longitud')
# plt.axis([0,1.1*sim.l,0,sim.e])
# plt.xlabel('L (m)')
# plt.ylabel('e%')
# plt.title('Longitud vs Caida de Tension')
# plt.show()

# grafica corriente vs caida de tension

xI = []
yI = []
for xi in sim.si:
    xI.append(xi[2])
    yI.append(xi[4])

# plt.plot(xI, yI, 'bo--', alpha=0.3, label='Corriente')
# plt.axis([0,1.1*sim.Ipc,0,sim.e])
# plt.xlabel('Ipc (A)')
# plt.ylabel('e%')
# plt.title('Corriente vs Caida de Tension')
# plt.show()

# termina bloque de prueba

plt.plot(xz, yz, 'ro--', alpha=0.3, label='Impedancia (ohm/km)')
plt.plot(xl, yl, 'go--', alpha=0.3, label='Longitud (m)')
plt.plot(xI, yI, 'bo--', alpha=0.3, label='Corriente (A)')
plt.ylabel('e%')
plt.title('Caída de Tensión')
plt.legend()
plt.show()
