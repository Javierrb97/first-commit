"""
Nombre: MainPunto.py
Objetivo: Muestra como trabajar en objetos con python
Autor: Francisco Javier Rios Barragan
Fecha: 30 de julio 2020 
"""



#INcluir el archivo de la clase

from Punto import Punto

#Creamos objetos dentro del mismo archivo
puntoA = Punto(0,0)
#INvocaos metodos get
print("El valor de la coordenada X es:",puntoA.getX())
print("El valor de la coordenada Y es:",puntoA.getY())
#invocamos metodos set
puntoA.setX(23)
puntoA.setY(12)
#IMprimos los valores de los atributos del objeto A
print(puntoA.toString())

#Creamos objetos dentro del mismo archivo
puntoB = Punto(-10,-20)
#INvocaos metodos get
print("El valor de la coordenada X es:",puntoB.getX())
print("El valor de la coordenada Y es:",puntoB.getY())
#invocamos metodos set
puntoA.setX(10)
puntoA.setY(20)
#IMprimos los valores de los atributos del objeto A
print(puntoA.toString())