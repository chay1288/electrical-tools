#! /usr/bin/python
# -*- coding: utf-8 -*-

# tabla de registros de calibre de conductores
# para programa calibre.py

def datos_calibres(cal, imp, a60, a75, secc, area):
  awg_calibre = [cal, imp, a60, a75, secc, area]
  return awg_calibre

def imprimir_tabla():
  tabla_cal = [head, awg14, awg12, awg10, awg8, awg6, awg4, awg2, awg1_0, awg2_0, awg4_0, awg250, awg300, awg350, awg400, awg500, awg600, awg750, awg1000]
  for i in tabla_cal:
    #print '%8s %12.6f %6.0f %6.0f %10s %10s'
    print i

head = ['Calibre', 'Impedancia', '60 C', '75 C', 'Seccion', 'Area']

awg14 = datos_calibres(14, 8.8582, 20, 20, 2.08, 9.62)

awg12 = datos_calibres(12, 5.5774, 25, 25, 3.3, 12.57)

awg10 = datos_calibres(10, 3.6089, 30, 35, 5.26, 16.62)

awg8 = datos_calibres(8, 2.2965, 40, 50, 8.36, 28.27)

awg6 = datos_calibres(6, 1.4763, 55, 65, 13.3, 47.78)

awg4 = datos_calibres(4, 0.9842, 70, 85, 21.15, 63.6)

awg2 = datos_calibres(2, 0.6561, 95, 115, 33.6, 86.6)

awg1_0 = datos_calibres('1/0', 0.4265, 125, 150, 53.48, 145.3)

awg2_0 = datos_calibres('2/0', 0.360892, 145, 175, 67.43, 172)

awg3_0 = datos_calibres('3/0', 0.308398, 165, 200, 85.01, 203.6)

awg4_0 = datos_calibres('4/0', 0.262467, 195, 230, 107.2, 243.3)

awg250 = datos_calibres(250, 0.239501, 215, 255, 126.7, 298.6)

awg300 = datos_calibres(300, 0.213254, 240, 285, 152, 343)

awg350 = datos_calibres(350, 0.196859, 260, 310, '---', 405.9)

awg400 = datos_calibres(400, 0.183727, 280, 335, 202.7, 430.1)

awg500 = datos_calibres(500, 0.164042, 320, 380, 253.4, 514.7)

awg600 = datos_calibres(600, 0.154199, 355, 420, '---', '---')

awg750 = datos_calibres(750, 0.141076, 400, 475, 380, 735.4)

awg1000 = datos_calibres(1000, 0.131233, 455, 545, 506.7, 934.8)

