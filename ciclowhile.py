#CICLO MIENTRAS

#DECLARAR UNA VARIABLE CENTINELA O VARIABLE DE CONTROL PARA EVALUAR LA EJECUCIÓN DE MI CICLO
i = 0

#MENÚ DE OPCIONES
print("***MENU***")
print("1. Saludar")
print("2. Despedir")
print("3. Contar quien ganó el clásico")
print("4. Contar si está lloviendo")
print("5. Salir")

#Programar la estructura del ciclo mientras
while(i!=0): # != es para definir diferente
    i=int(input("Digite una opción del menú: "))
    print("estoy saltando cuerda",i)
    if(i==1):
        print("Hola cómo estás")
    elif(i==2):
        print("Chao amor")
    elif(i==3):
        print("Ganador el ROJO")
    elif(i==4):
        print("No llueve en Medallo")
    elif(i==5):
        break
    else:
        print("Digite una opción válida")
print("Salimos del while")