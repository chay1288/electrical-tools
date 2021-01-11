# CalibrAWG


_**Para uso didáctico.**_

Cálculo de calibre de conductores de eléctricos en circuitos derivados de 
acuerdo a tres criterios establecidos en la NOM-001-SEDE-2012 de México. Los
criterios son Ampacidad del conductor, Caída de Tensión en el conductor y 
Corriente de Cortocircuito soportado por el conductor.

El cálculo es para conductores de cobre tipo THW, THHW y THHW-LS con 
temperaturas de 60ºC, 75ºC y 90ºC.

Las unidades en que se realizan los cálculos son con SI (Sistema Internacional)


### Forma de Uso del CLI

Ejecute su intérprete de python y diríjase a la carpeta `calibrAWG` y ejecute
el archivo `menu_cli.py`.

Del menú seleccione la opción deseada.

1. Crea un nuevo circuito derivado
2. Busca en la base de datos un circuito derivado de acuerdo a su ID
3. Lista todos los circuitos en la base de datos
4. Guarda los resultados del circuito actual en un archivo `.txt`
5. Exporta la base de datos en un archivo `.csv`
6. Termina el programa

Cuando selecciona la opción 1 (Nuevo Circuito Derivado) le preguntará por los
datos del circuito, recuerde que las unidades que maneja son del SI.
Voltaje (V), Potencia (W), Longitud (m), Temperatura (ºC), Corriente (A).

El resultado del calibre está dado en AWG (American Wire Gauge), que es como se
comercializa en México.

Además del calibre del conductor, calcula también el interruptor de protección
y el conductor de puesta a tierra.


### Lista de Versiones

> `v0.0.9-alpha` Escrito originalmente en `Python 2.7`
>
> `v0.1.0-beta` Portada a `Python 3.4` funciona en la línea de comandos (CLI).
>
> `v0.2.0-beta` Implementa una función rudimentaria de Interfaz gráfica (GUI).
Funciona en `Python 3.6.9`


### To-Do

- Mejorar las funciones del menú de la CLI
- Continuar la implementación de la GUI
- Continuar con la funciones de la simulación
- Implementar la simulación en la GUI
