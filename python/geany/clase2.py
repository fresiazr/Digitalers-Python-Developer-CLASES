#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Potencia")
print(2 ** 10)

print("Raíz")
print(8 **(1/3)) #3 porque es una raíz cúbica

resultado = ((3+2)/(2*5)) ** 2
print("El resultado es: ", resultado)

"""
edad = int(input("Cuantos años tenes: "))
print(type(edad))

edad +=1

print(edad)
"""

"""
entrada1 = input("Ingresar Cadena 1: ")
entrada2 = input("Ingresar Cadena 2: ")

if entrada1 == entrada2:
	print("Las cadenas son iguales")
else:
	print("Las cadenas son desiguales")
"""

"""
nombre = input("Ingresar nombre: ")

if nombre != "":
	print("El nombre se ingreso correctamente.")
else:
	print("ERROR")
"""

#BUCLE WHILE / mientras

"""
control = 0

while True:
	if control < 5:
		print("hola")
		control +=1
	else:
		break  
	
print("Se termino el bucle")
"""

control = 0

"""
while control < 10:
	print(control)
	control +=1
"""
	
# O

while True:
	if control < 10:
		print(control)
		control +=1	
	else:	
		print("Se termino el bucle")	
		break

#Si se usa while True se tiene que poner break

#ARRAY / lista

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista2 = ["Pedro", "Luciana", "Josefina"]

lista3 = ["CABA", 3, True, 2.5]

#LISTA 1
print(lista1[5]) #Imprime la posición 5 / valor 6
print(len(lista1)) #cantidad de elementos que tiene la lista

#LISTA 2
print(lista2)
lista2.append("Juan")

print(lista2)
lista2.insert(1, "Juan") #insert (número de índice, nombre)
print(lista2)

del lista2[-1] #accedes a la última de la lista
print(lista2)

lista2.remove("Pedro")
print(lista2)

#LISTA 3
print(len(lista3)) #total de posiciones
print(lista3[len(lista3) -  1]) #último valor
