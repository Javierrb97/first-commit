"""
Nombre: Punto.py
Objetivo: Muestra como trabajar en objetos con python
Autor: Francisco Javier Rios Barragan
Fecha: 30 de julio 2020 
"""



class Punto(self):

        #Definir una especie de constructor
        def __init__ (self, valorX, valorY):
            #Definimos el nombre de los atributos
            self.x = valorX
            self.y = valorY

        #Lista de metodos get
        def getX(self):
            return self.x

        def getY(self):
            return self.y

        #Lista de metodos set
        def setX(self, valorX):
            #Asignar el argumento al atributo
            self.x = valorX

        def setY(self, valorY):
            self.y = valorY

        #Metodo tiString: regresa los vlores de los atributos
        def toString(self):
            return "Las coordenadas X,Y del punto son : ",+ str( self.getX()),+ " , "+str(self.getY())
    #Fin de clase

    