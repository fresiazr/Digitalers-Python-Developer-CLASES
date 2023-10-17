#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TKINTER ---> TK INTER

import tkinter as tk

"""
def funcion_boton():
	nombre = caja.get()
	etiqueta_nombre.config(text= "Hola soy " + nombre + "!")

ventana = tk.Tk() # Crea la ventana // PRINCIPIO DE LA APP

ventana.config(width = 400, height = 400) # Crea la ventana
ventana.title("Aplicación de escritorio") # Le asigna un título

boton = tk.Button(ventana, text = "Botón", command=funcion_boton) # Crea un botón // La ventana se tiene que especificar si hay varias
boton.place(x = 20, y = 120, width = 100, height = 25) # Ubica el botón en la ventana

caja = tk.Entry() # Crea una caja de texto
caja.place(x = 20, y = 50, width = 200, height = 25) # Ubica la caja en la ventana

etiqueta = tk.Label(text = "Ingresa tu nombre:", bg= "#90EE90", width = 50) # Crea una etiqueta
etiqueta.place(x = 20, y = 20) # Ubica la etiqueta en la ventana

etiqueta_nombre = tk.Label() # Etiqueta nombre
etiqueta_nombre.place(x = 20, y = 200)

ventana.mainloop() # La hace visible // FIN DE LA APP
"""

def sumar():
	n1 = int(caja1.get())
	n2 = int(caja2.get())
	resultado = n1 +n2
	etiqueta_resultado.config(text = "El resultado es " + str(resultado) + ".")

ventana = tk.Tk() # Crea la ventana // PRINCIPIO DE LA APP

ventana.config(width = 400, height = 400) # Crea la ventana
ventana.title("Aplicación de escritorio") # Le asigna un título

# BOTÓN
boton = tk.Button(ventana, text = "Suma", command=sumar) # Crea un botón // La ventana se tiene que especificar si hay varias
boton.place(x = 100, y = 120, width = 75, height = 25) # Ubica el botón en la ventana

# PRIMER NUMERO
caja1 = tk.Entry()
caja1.place(x = 20, y = 50, width = 50, height = 25)

etiqueta1 = tk.Label(text = "Ingresa un número:", bg= "#90EE90")
etiqueta1.place(x = 20, y = 20)

# SEGUNDO NUMERO
caja2 = tk.Entry()
caja2.place(x = 200, y = 50, width = 50, height = 25)

etiqueta1 = tk.Label(text = "Ingresa otro número:", bg= "#EE90CF")
etiqueta1.place(x = 200, y = 20)

etiqueta_resultado = tk.Label()
etiqueta_resultado.place(x = 100, y = 200)

ventana.mainloop() # La hace visible // FIN DE LA APP
