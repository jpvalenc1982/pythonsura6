#CICLO MIENTRAS

#DECLARAR UNA VARIABLE CENTINELA O VARIABLE DE CONTROL PARA EVALUAR LA EJECUCIÓN DE MI CICLO
import math
i = 0
numero1=0
numero2=0

#MENÚ DE OPCIONES
print("***MENU***")
print("1. Sumar dos números")
print("2. Restar dos números")
print("3. Encontrar la raíz cuadrada de un número")
print("4. Multiplicar dos números")
print("5. Salir")

#Programar la estructura del ciclo mientras
while(i!=5): # != es para definir diferente
    i=int(input("Digite una opción del menú: "))
    if(i==1):
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print ("La suma entre ",numero1," y ",numero2,"es de ",str(numero1+numero2))
    elif(i==2):
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print ("La resta entre ",numero1," y","numero2","es de ",str(numero1-numero2))
    elif(i==3):
        numero1 = int(input("Ingrese un número: "))
        print ("La raíz cuadrada de ",numero1," es de",math.sqrt(numero1))
    elif(i==4):
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print ("La multiplicación entre ",numero1," y ",numero2,"es de ",str(numero1*numero2))
    elif(i==5):
        break
    else:
        print("Digite una opción válida")
print("Salimos del while")