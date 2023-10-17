#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
EJERCICIO
materias=["Matematicas","Fisica","Quimica","Historia"]
notas=[] 
i=0

for materia in materias:
nota=int(input("ingresa la nota sacaste en "+ materia+ ": "))

while nota<=0:
print("error la nota debe ser mayor a ´0´, ingrese otra nota")

nota=int(input("ingresa la nota sacaste en "+ materia+ ": "))
notas.append(nota)

for materia in materias:
print("en ", materia, " sacaste ", notas[i])
i=i+1
"""

letras = ["a", "b", "c", "d"]
letras[0] = "A"

ceros = [0] * 10
print(ceros)

combinada = ceros + letras
print(combinada)

#Los Strings son iterables

print(letras)
print(letras [0:3]) #Imprime los indices de 0 y 3
            
numeros = [1, 2, 3, 4, 5, 6, 7, 8] #Imprime de 2 en 2
print(numeros[::2])                #[::3] 3 en 3, etc

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros[::-1])               #Imprime la lista al revez

numeros.clear() #Elimina toda la lista por completo
                #Se imprimen los corchetes vacios
                
numeros_numeros = [1, 2, 3, 4, 4, 4, 4, 4]
#Variable primero guarda el primer indice,
#La variable segundo el segundo y 
#La variable *otros los demás
primero, segundo, *otros = numeros_numeros

print(primero, segundo)
print(otros)               

letras.sort() #Ordena por órden alfabético
numeros_numeros.sort(reverse=True) #Imprime la lista al revez

"""
Se tiene una lista de nombres y se desea recorrer con un 
bucle for. Ordenar de mayor a menor (Z-A) e imprimir 
por pantalla cada elemento
"""

nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]

nombres = ["Agustina", "Marisa","Juan", "Osvaldo"]
for nombre in nombres:
	nombres.sort(reverse =True)
	print(nombres)

"""
Escribir un programa dque pida al ususario una palabra y
muestre por pantalla el número de veces que contiene
cada vocal
"""

"""
palabra = input("Ingrese una palabra: ").lower()
vocales = ["a", "e", "i", "o", "u"]
cantidad = [0, 0, 0, 0, 0]

for letra in palabra :
	for i in range(len(vocales)):
		if letra == vocales[i]:
		 cantidad[i] += 1
	for vocal in vocales:
		print(vocal + ": " + str(cantidad[vocales.index(vocal)])) 
"""

#MATRIZ
"""
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]


fila=int(input("ingrese una fila : "))
columna=int(input("ingrese una columna : "))

if fila<=len(matriz):
	print("en la posicion ",fila,",",columna,"se encuentra el numero : ", matriz[fila][columna])
else:	
	print("error rango fuera de la matriz")
"""

alumnos = ["Matias", "Jorge", "Martin", "Pablo"]
for alumno in alumnos:
 print("Hola mundo")
