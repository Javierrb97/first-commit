"""
Nombre: Circunferencia.py
Objetivo: Muestra como trabajar en objetos con python
Autor: Francisco Javier Rios Barragan
Fecha: 30 de julio 2020 
"""

import math
from Punto import Punto

class Circunferencia(Punto):
    #Constructor
    def __init__(self, valorX, valorY, vRadio):
            #Aributos de Punto
            Punto.__init__(self, valorX, valorY)
            #Atributo de la Circunferencia
            self.radio = vRadio

    def getRadio(self):
        return radio

    def setRadio(self, vRadio):
        self.radio = vRadio

    def getArea(self):
        return math.pi*math,pow(self.radio, 2)
    
    def toString(self):
        return Punto.toString(self)+ "Y el valor del radio es: "+ str(self.radio)

print("hola")
c = Circunferencia(2,3, 10)
print(c.toString())