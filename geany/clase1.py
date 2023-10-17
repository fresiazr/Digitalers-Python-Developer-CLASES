#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("hola mundo")

print(2 + 3)

#Concatenación#
a = 2
print(type(a))
print("número " + str(a))

d = "hola"
e = "a"
f = "todos"

print(d + " " + e + " " + f)

#Ejercicio 1#
a = 3 + 2
b = 7 - 4
c = 4 * 2

resultado = a + b + c

print("variable a")
print(a)
print("variable b")
print(b)

print("variable c")
print(c)

print("variable resultado")
print(resultado)

#Ejercicio 2#
saludo = "hola "
nombre = "fresia"

mensaje = saludo + nombre

print(mensaje)

r = 1

print(r > 1 and r == 0) 
#ambas condiciones tienen que ser verdaderas
#CONJUNCIÓN

print(r > 1 or r == 0)
#a es una cosa o la otra / comparación
# DISYUNCIÓN
 
p = 5
print(not p == 10)
print(p !=10) 

x = 5
if x == 10:
	print("el valor de x es 10")
elif x == 12:
    print("el valor de x es 12")
else:
	print("el valor de x NO es 10 NI 12")

#Ejercicio 3#
texto_1 = "potente"
texto_2 = "sol"
texto_3 = "triunfo"

print ("el " + texto_2 + " es muy " + texto_1 + "; estar bajo sus rayos se siente como un " + texto_3)

#Ejercicio 4#
dividendo = 2.3
divisor = 4.5

if divisor == 0:
	print("ERROR")
else:
	print(dividendo/divisor)

#Ejercicio 5#
base = 10
altura = 5

area = base*altura

#la coma separa las 2 variables distintas
#String e int
print("el resultado es: ", area)

#Ejercicio 6#
h = 20
j = 10

print("suma", h + j)
print("resta", h - j)
print("multiplicación", h * j)
print("división", h / j)
print("modulo", h % j)

""" 
Bloque de cometario
Triple comilla
"""

