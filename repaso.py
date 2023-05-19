from os import system
system("cls")
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
Telefono = input("Ingrese su numero de telefono: ")
print(f"Su nombre es: {nombre} Y su edad es: {edad} Su ciudad es: {ciudad} Y su numero de telefono es: {Telefono}")
lista1 = list(["seba","ola k pasa"])
num = [1,200,500,400,200,20000]
print (lista1,num)
print("\n")#salto en linea
nombre2 = input("Ingrese su segundo nombre: ")
edad2 = input("Ingrese otra edad:")
ciudad2 = input("Ingrese otra ciudad: ")
Telefono2 = input("Ingrese otro telefono: ")
datos_usuario = {
    "Nombres":nombre2,
    "Edad":edad2,
    "Ciudad":ciudad2,
    "Telefono":Telefono2,}
print("Estos son los datos almacenados en diccionario",datos_usuario)
print("\n")
print(type(datos_usuario))
tupla=tuple()
tupla = ("seba",100,"ola",900)
print("Estos son los datos de la tupla: ",tupla)
print(type(tupla))
print("\n")

pruebaSET = {"gato","azul","perro"}
print("Esto en lo que se almacena en el set",pruebaSET)

print(type(pruebaSET))


