#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Ejercicio 1")
"""
Tomás rindió 3 exámenes.
Mostrar el promedio por pantalla.
"""

nota_uno = 10
nota_dos = 6
nota_tres = 8

sumanotas = nota_uno + nota_dos + nota_tres
promedio = sumanotas/3

print("El promedio de Tomas es: ", promedio)

print("Ejercicio 2")
"""
Hacer un programa que determine si una persona 
es menor de edad o mayor de edad, teniendo la edad en una variable.
Probar el código cambiando el valor de la variable “edad”.
"""

edad = 24

if edad > 75:
	print("La edad es mayor")
else:
	print("La edad es menor")

print("Ejercicio 3")
"""
Un empleado cobró 300 dólares por mes desde enero a junio, 500 dólares
de julio a octubre, y 700 dólares por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares
"""

"""
sueldo_enejun = 300*6
sueldo_juloct = 500*4
sueldo_novdic = 700*2

sueldo_total = sueldo_enejun + sueldo_juloct + sueldo_novdic
sueldo_promedio = sueldo_total/3
"""

#MAL es dividido 12 porque es el sueldo de todo el año !!!

sueldo_enejun = 300*6
sueldo_juloct = 500*4
sueldo_novdic = 700*2

sueldo_promedio = (sueldo_enejun + sueldo_juloct + sueldo_novdic)/12

print("El promedio del sueldo es: ", sueldo_promedio)

if sueldo_promedio <= 300:
	print("El empleado cobra un sueldo bajo.")
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
	print("El empleado cobra un sueldo normal.")
elif sueldo_promedio >= 900:
	print("El empleado cobra un sueldo mejor de lo normal")

