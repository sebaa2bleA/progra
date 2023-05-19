a = 20
b = 5
c= 4


print("###### 03 OPERADORES ARITMETRICOS ######")
print("Suma entre a + b es:",a+b)


t = 5.39
g = 9.81

v = g * t
print("La velocidad del objeto en caida libre es de: {v} n/s")


##operadores de comparacion
print("###### 02 OPERADORES DE COMPRARCION ######")
print("a = b") #igual a
print("a != b") #desigual a 
print("a > b") #mayor que
print("a < b") # menor que 
print("a >= b")#mayor o igual que
print("a <= b") #menor o igual que


animal_domestico = "gato"
animal_salvaje = "leopardo"
print(animal_domestico = animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

##Operadores logicos
bencina = True
encendido = True 
edad = 19

##Utilizando operacion and
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

##utlizando operacion or
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

##Utlizando operacion NOT
if not bencina and encendido:
    print("El vehiculo  puede avanzar")
else:
    print("El vehiculo no puede arrrancar")


##utilizando el operador NOT junto al and y or
if not bencina or (encendido and edad >=18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    