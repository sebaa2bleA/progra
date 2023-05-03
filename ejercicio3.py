from os import system
system("cls")
num1=int(input("Ingrese un Número: "))
num2=int(input("Ingrese un segundo Número: "))
num3=int(input("Ingrese un tercer Número: "))
if num1 > num2 and num1 > num3:
    print("El numero mayor es: ",num1)
elif num2 > num1 and num2 > num3:
    print("El Número mayor es: ",num2)
elif num3 > num1 and num3 > num2:
    print("El Número mayor es:",num3)
else:
    print("No se pudo establecer el mayor")