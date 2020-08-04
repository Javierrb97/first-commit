"""
Nombre: Cilindro.py
Objetivo: Muestra como trabajar en objetos con python
Autor: Francisco Javier Rios Barragan
Fecha: 30 de julio 2020 
"""

from CIrcunferencia import Circunferencia

class Cilindro(Circunferencia):
    #Definimos el constructor
    def __init__(self, valorX, valorY, vRadio):
        #constructor de Circunfeencia
        Circunferencia.__init__(self, valorRadio)
        #constructor de CIlindro
        self.altura = valorAltura

    def getAltura(self):
        return self.altura
    
    def setAltura(self, valorAltura):
        self.altura = valorAltura

    def getVolumen(self):
        return (Circunferencia.getArea(self) * self.getAltura())
    
    def toString(self):
        return Circunferencia.toString(self)+ "Y la altura es:"+str(self.altura) + "el volumen es:" + self.getVolumen()

c = Cilindro(2,3,4,7)
print(c.toString())