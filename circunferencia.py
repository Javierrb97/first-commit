
"""
Nombre: Circunferencia.py
Objetico: Permite calcular el area de una circunferencia
Autor:
Fecha: 28 de julio del 2020
"""

#IMportamos libreria math
import math

#-------------------------------------
#Funcion para calcular area
#-------------------------------------
def calcularArea(valorRadio):
	return math.pi*math.pow(valorRadio,2)


#MOdulo principal
def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':
		print ("--- Programa para calcular area de circunferencia---")
		vradio = int(input("Introduce valor del radio:"))
		print ("El area de la circunferenia con radio igual a: {},es: {}".format(vradio, calcularArea(vradio)))
		ciclo = input ("¿Otro calculo (s/n)")
	else:
		print ("*** FIn del programa...")


if __name__ == "__main__":
	main()
