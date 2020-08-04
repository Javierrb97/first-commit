
"""
Nombre: funciones.py
Objetivo: Muestra la operación de las funciones en python
Autor:
Fecha: 27 de julio de 2020
"""

def mensaje():
	print ("hola desde mensaje")

def regresaMensaje():
	return "saludo desde regresaMensaje"

def printMensaje(msg):
	print (msg)

def suma (n1, n2):
	return n1+n2

def resta(n1, n2):
	return n1-n2

def multiplicacion(n1, n2):
	return n1*n2

def division(n1, n2):
	if (n2 !=0):
		return n1/n2
	else:
		print ("Error, no se puede dividir entre cero...")

def compara(n1, n2):
	if n1>n2:
		print ("El mayor es n1: ", n1," ", n2)
	elif n2>n1:
		print ("EL amyor es : {},{}".format(n2,n1))
	else
		print ("Los numeros son iguales: {}, {}".format(n1,n2))

#FUncion para mostrar operacion de for
def cuenta(n1, n2):
	if(n2>n1):
		for i in range (n1, n2+1):
			print("Valor de i:{}".format(i))
	elif(n1>n2):
		for i in range (n1, n2-1, -1):
			print("Valor de i:{}".format(i))
	else:
		print ("LOs numeros son iguales, no puedo contar {}, {}".format(n1, n2))

def main():
	ciclo = 'S'
	while ciclo == 'S' or ciclo == 's':

		#Invocamos función mensaje
		mensaje()
		#Invocamos función regresaMensaje
		print (regresaMensaje)
		#Invocamos funcion printMensaje
		printMensaje("hola te saludo...")

		#Leemos los datos por teclado
		a = int(input("Ingresael primer entero"))
		b = int(input("Ingresael segundo entero"))
		#Invocamos la funcion suma
		print ("La suma es: ", suma(a,b))
		print ("La resta es: ", resta(a,b))
		print ("La multiplicacion es: ", multiplicacion(a,b))
		print ("La division es: ", division(a,b))

		cuenta(a,b)
		compara(a,b)
		#Preguntamos por otra operación
		ciclo = input("¿Desea otra operacion (s/n)")


	else:
		print ("*** FIn de programa")

if __name__ == "__main__":
	main()
