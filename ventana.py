"""
Nmbre: ventana.py
Objetivo: Muestra como trabajar con ventanas gui en python y tkinter
Autor:
Fecha: 29 de julio de 2020
"""

#IMportar las librerias de tkinter
from tkinter import *
from tkinter import ttk

#Funcion para enviar datos al servidor echo
def sendToServer():
	print("Enviado ...")


#Funcion main
def main():
	#CReamos la ventana contenedora
	win = Tk()
	#Modificamos parametros de la ventana win
	win.geometry("400x400")
	win.title("MI primer ventana en Python Tkinter")

	#Creamos una etiqueta
	label = ttk.Label(win, text="Texto a enviar al Servidor").pack(side=TOP)
	txtCampo =ttk.Entry(win).pack(side=TOP)

	#Creamos un boton para enviar el contenido de la propiedad text del entry al servidor
	ttk.Button(win, text="Enviar mensaje", command=sendToServer).pack(side=BOTTOM)

	#Creamos un boton y lo colocamos en la ventana
	ttk.Button(win, text="Salir",command=quit).pack(side=BOTTOM)

	#Hacemos un ciclo para dibujar y esperar eventos
	win.mainloop()

	




#Para funcion main

if __name__ == "__main__":
	main()
