#! /usr/bin/python
# -*- coding: utf-8 -*-

# tabla de registros de calibre de conductores
# para programa calibre.py

def datos_calibres(cal, imp, a75, a90, secc, area):
	awg_calibre = [cal, imp, a75, a90, secc, area]
	return awg_calibre

def imprimir_tabla():
	tabla_cal = [awg14, awg12, awg10, awg8, awg6, awg4, awg3, awg2, awg1, awg1_0, awg2_0, awg4_0, awg250, awg300, awg350, awg400, awg500, awg600, awg750, awg1000]
	#for i in tabla_cal:
		#print '%8s %12.6f %6.0f %6.0f %10s %10s'
		#print i
	return tabla_cal

head = ['Calibre', 'Impedancia', '75 C', '90 C', 'Seccion', 'Area']

awg14 = datos_calibres(14, 8.8582, 20, 25, 2.08, 8.968)

awg12 = datos_calibres(12, 5.5774, 25, 30, 3.31, 11.68)

awg10 = datos_calibres(10, 3.6089, 35, 40, 5.26, 15.68)

awg8 = datos_calibres(8, 2.2965, 50, 55, 8.37, 28.19)

awg6 = datos_calibres(6, 1.4763, 65, 75, 13.3, 46.84)

awg4 = datos_calibres(4, 0.9842, 85, 95, 21.2, 62.77)

awg3 = datos_calibres(3, 0.7900, 100, 115, 26.7, 73.16)

awg2 = datos_calibres(2, 0.6561, 115, 130, 33.6, 86.00)

awg1 = datos_calibres(1, 0.5200, 130, 145, 42.4, 122.60)

awg1_0 = datos_calibres('1/0', 0.4265, 150, 170, 53.49, 143.40)

awg2_0 = datos_calibres('2/0', 0.360892, 175, 195, 67.43, 169.30)

awg3_0 = datos_calibres('3/0', 0.308398, 200, 225, 85.01, 201.10)

awg4_0 = datos_calibres('4/0', 0.262467, 230, 260, 107.2, 239.90)

awg250 = datos_calibres(250, 0.239501, 255, 290, 127.0, 296.50)

awg300 = datos_calibres(300, 0.213254, 285, 320, 152.0, 340.70)

awg350 = datos_calibres(350, 0.196859, 310, 350, 177.0, 384.40)

awg400 = datos_calibres(400, 0.183727, 335, 380, 203.0, 427.00)

awg500 = datos_calibres(500, 0.164042, 380, 430, 253.0, 509.70)

awg600 = datos_calibres(600, 0.154199, 420, 475, 304.0, 627.70)

awg750 = datos_calibres(750, 0.141076, 475, 535, 380.0, 751.70)

awg1000 = datos_calibres(1000, 0.131233, 545, 615, 507.0, 953.80)

