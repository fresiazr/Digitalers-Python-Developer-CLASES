#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FUNCIONES

def suma(numero1, numero2):
	return numero1 + numero2

#dejar 2 renglones	

resultado_s = suma(2, 3)
print(resultado_s)

resultado_s2 = suma(5, 2)
print(resultado_s2)

simbolos = ["HOLA"]

def imprimir(lista, minimo, maximo, volumen):
	for elemento in lista:
		print("El símbolo " + elemento + " tuvo un precio mínimo de "
		+ str(minimo) + " precio máximo de " + str(maximo) + 
		" y un volumen total de " + str(volumen) + " durante el día.")


print("Simbolos:")
imprimir(simbolos, 366, 377.5, 1349.28)

#Escribir una función que reciba una lista de números
#y devuelvaotra lista con sus cuadrados

lista1 = [2, 4, 6, 8, 10, 12]
lista2 = []

def lista_al_cuadrado(lista1):    	  
	for num in lista1:
		lista2.append(num**2)
	return lista2
	
cuadrados = lista_al_cuadrado(lista1)

print("Lista 1: ", lista1)
print("Lista 2: ", cuadrados)

"""
Escribir una función que calcule el total de
una factura tras aplicarle el IVA.
La función debe recibir por parámetro la cantidad SIN
iva y el porcentaje del impuesto a aplicar. 
Finalmente debe devolver el total del valor de la 
factura.Si se invoca la función sin pasarle el 
porcentaje de IVA, deberá aplicar por defecto el 21%
"""

def factura(cantidad, iva = 21/100):
	 return cantidad + cantidad * iva

monto = 1000
print("monto: $", monto)
print("monto con iva: $", factura(monto))


def min_y_max(lista):
	a = min(lista)
	b = max(lista)
	return [a, b]	

print(min_y_max([4, 6, 2, 7, 0, 2]))


texto = "Hola que tal"
texto = texto.split()
lista = []

for i in texto:
	lista.append(i)
	
print(lista)

"""
Escribir un programa que reciba un string 
y que devuelva otra lista con cada palabra que 
contenga como items separados dentro de la lista.
Escribir otra función que reciba la nueva lista 
generada y elimine las palabras repetidas. 

frase = "Como quieres que te quiera si el que 
quiero que me quiera no me quiere como quiero que
me quiera"
"""

frase = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"

def separar(frase):
	lista = []
	frase= frase.split()
	
	for i in frase:
		lista.append(i)
	return lista
	

def repeticion(list):
	list_rep=[]
	
	for i in list:
		if i not in list_rep:
			list_rep.append(i)
	return list_rep
	
lista_separada=separar(frase)
lista_sin_repeticiones = repeticion(lista_separada)
print("la lista separada es: ", lista_separada)
print("la lista de palabras sin repeticiones es: ", lista_sin_repeticiones)

# LIBRERIAS ESTANDAR

import time, random

print(time.asctime())
time.sleep(5)

print(random.randint(2, 18))
