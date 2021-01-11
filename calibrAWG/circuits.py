#!/usr/bin/python
# -*- coding: utf-8 -*-

import calc
import datetime

last_id = 0

class Circuit:
    """Creador de datos de circuitos result"""
    db_circuits = []

    def __init__(self, name="Circuito"):
        self.date = datetime.datetime.now()
        global last_id
        last_id += 1
        self.id = last_id
        self.name = name+str(self.id)
        self.db_circuits.append([self.id,self.date,self.name])

    def prompt(self):
        """Datos proporcionados por el usuario para el calculo"""
        print('=================================================================')
        self.fn  =   int(input(' Fases                                      = '))
        self.v   = float(input(' Voltaje                                    = '))
        self.p   = float(input(' Potencia                                   = '))
        self.fp  = float(input(' Factor de Potencia                         = '))
        self.n   = float(input(' Eficiencia                                 = '))
        print('-----------------------------------------------------------------')
        self.l   = float(input(' Longitud                                   = '))
        self.e   = float(input(' Caida de tension deseada                   = '))
        print('-----------------------------------------------------------------')
        self.CTC =   int(input(' Conductores en tuberia conduit             = '))
        self.Ta  = float(input(' Temperatura ambiente                       = '))
        print('-----------------------------------------------------------------')
        self.Tc  = float(input(' Temperatura del conductor                  = '))
        self.Tcc = float(input(' Temperatura de cortocircuito del conductor = '))
        self.ccc = float(input(' Ciclos del cortocircuito                   = '))
        self.tcc = self.ccc/60.0
        self.Icc = float(input(' Corriente de cortocircuito                 = '))
        print('=================================================================')

        self.data_input = [
            self.fn, self.v, self.p, self.fp, self.n,
            self.l, self.e,
            self.CTC, self.Ta,
            self.Tc, self.Tcc, self.ccc, self.tcc, self.Icc]

        for i in self.db_circuits:
            if self.id is i[0]:
                index_id = self.db_circuits.index(i)
                self.db_circuits[index_id].append(self.data_input)

    def compute(self):
        """Computo de los datos para obtener el calibre del conductor AWG"""
        self.kFase   = calc.alimentacion(self.fn)
        self.TC      = calc.temp_cond(self.Tc)
        self.ft      = calc.fct(self.Ta, self.TC)
        self.fa      = calc.fca(self.CTC)

        self.ipc     = calc.corriente_plena_carga(self.p, self.v, self.fp, self.n, self.kFase[1])
        self.ampmin  = calc.ampacidad_minima(self.ipc, self.TC)
        self.ampc    = calc.ampacidad_corregida(self.ipc, self.fa, self.ft, self.TC)
        self.awg_amp = calc.conductor_ampacidad(self.ampmin[3], self.ampc[3])

        self.Zmaxp   = calc.impedancia_maxima_permitida(self.e, self.v, self.l, self.ipc, self.kFase[0])
        self.awg_imp = calc.conductor_impedancia(self.Zmaxp)

        self.sicc    = calc.seccion_cobre_icc(self.Icc, self.Tc, self.Tcc, self.tcc)
        self.awg_icc = calc.conductor_cortocircuito(self.sicc)

        self.awg     = calc.conductor_AWG(self.awg_amp[1], self.awg_imp[1], self.awg_icc[1])
        self.ereal   = calc.caida_tension(self.awg[1], self.kFase[0], self.ipc, self.l, self.v)

        self.itm     = calc.proteccion_ITM(self.ipc)
        self.awg_cpt = calc.conductor_puesta_tierra(self.itm)

        self.compute_data = [
            self.kFase, self.TC, self.ft, self.fa,
            self.ipc, self.ampmin, self.ampc, self.awg_amp,
            self.Zmaxp, self.awg_imp,
            self.sicc, self.awg_icc,
            self.awg, self.ereal,
            self.itm, self.awg_cpt]

        for i in self.db_circuits:
            if self.id is i[0]:
                index_id = self.db_circuits.index(i)
                self.db_circuits[index_id].append(self.compute_data)

    def show_results(self):
        """Computo de los datos para obtener el calibre del conductor AWG"""
        self.reporte = [
        (" "),
        ("================================================================="),
        ("Fecha : " +str(self.date.day)+"/"+str(self.date.month)+"/"+str(self.date.year)),
        ("Hora  : " +str(self.date.hour)+":"+str(self.date.minute)+":"+str(self.date.second)),
        ("ID    : " +str(self.id)),
        ("================================================================="),
        ("Resumen de "+str(self.name)+" :"),
        (" "),
        (" Voltaje = "+str(self.v)+" V @ "+str(self.fn)+" F 	Potencia = "+str(self.p)+" W"),
        (" FP = "+str(self.fp)+"	Eficiencia = "+str(self.n)+"	Longitud = "+str(self.l)+" m"),
        (" Corriente Nominal [Inom]  = "+str(self.ipc)+" A"),
        (" Ampacidad Minima [Amin]   : "),
        ("      Corriente Minima     = "+str(self.ampmin[0])+" A"),
        ("      Calibre              : "+str(self.ampmin[1])+" AWG"),
        ("      Ampacidad            : "+str(self.ampmin[2])+" A @ "+str(self.Tc)+" C"),
        (" Ampacidad Corregida [Ac]  : "),
        ("      Corriente Corregida  = "+str(self.ampc[0])+" A"),
        ("      Calibre              : "+str(self.ampc[1])+" AWG"),
        ("      Ampacidad            : "+str(self.ampc[2])+" A @ "+str(self.Tc)+" C"),
        (" Impedancia Maxima Permitida [Zmax]  = "+str(self.Zmaxp)+" ohm/km"),
        (" Seccion de cobre para Cortocircuito = "+str(self.sicc)+" mm2"),
        ("-----------------------------------------------------------------"),
        (" CALIBRE por Ampacidad     : "+str(self.awg_amp[0])+" AWG"),
        (" CALIBRE por Impedancia    : "+str(self.awg_imp[0])+" AWG"),
        (" CALIBRE por Cortocircuito : "+str(self.awg_icc[0])+" AWG"),
        ("-----------------------------------------------------------------"),
        (" CALIBRE Seleccionado      : "+str(self.awg[0])+" AWG"),
        ("      Ampacidad            : "+str(self.awg[self.TC+2])+" A @ "+str(self.Tc)+" C"),
        ("      Ampacidad Corregida  : "+str(self.awg[self.TC+2]*self.fa*self.ft)+" A @ "+str(self.Tc)+" C"),
        ("      Impedancia           : "+str(self.awg[1])+" ohm/km"),
        ("      Seccion de cobre     : "+str(self.awg[5])+" mm2"),
        ("      Seccion de aislante  : "+str(self.awg[6])+" mm2"),
        (" Caida de Tension estimada = "+str(self.ereal)+"%"),
        ("-----------------------------------------------------------------"),
        (" ITM de proteccion         : "+str(self.fn)+" x "+str(self.itm)+" A"),
        ("-----------------------------------------------------------------"),
        (" Conductor de Tierra       : "+str(self.awg_cpt[0])+" AWG"),
        ("================================================================="),
        (" ")]

        for i in self.reporte:
            print (i)

    def search(self,id):
        """Busca los datos de un circuito en base a su ID"""
        for i in self.db_circuits:
            if id is i[0]:
                print('    ID:',i[0])
                print(' Fecha:',i[1].year,'/',i[1].month,'/',i[1].day)
                print('  Hora:',i[1].hour,':',i[1].minute,':',i[1].second)
                print('Nombre:',i[2])
                print('=================================================================')

    def list_all_circuits(self):
        """Imprime todos los circuitos creados en la sesion"""
        print(' ')
        print('=================================================================')
        for i in self.db_circuits:
            print('    ID:',i[0])
            print(' Fecha:',i[1].year,'/',i[1].month,'/',i[1].day)
            print('  Hora:',i[1].hour,':',i[1].minute,':',i[1].second)
            print('Nombre:',i[2])
            print('-----------------------------------------------------------------')
            print(' ')
        print('=================================================================')

