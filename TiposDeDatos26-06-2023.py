edad = 29 #Enteros
estatura = 1.71 # Real
peso = 70.5
complejo = 1 + 4j #complejo
print("######1.-DATOS NUMERICOS ######");
print(f"Mi estatura es de {estatura} y mi peso es de{peso}")
print("Impresion de un numero complejo",complejo,"\n")

##Transformacion de valor real a entero
print(peso)
print("transformando un valor real a entero: ",int(peso))

##Transformando un entero a real
print("tranformando un valor entero a real: ",float(edad))

##operacion aritmetica basica
imc = peso / (estatura**2)
print("Mi imc es de; ",imc,"\n")

print("Mi imc es de: {:.2f}".format(imc),"\n")##para dar formato especifico a la salida de datos


##02 datos de tipo cadena de caracteres
asignatura = "Programacion"
carrera = "ingrenieria civil en informatica"
print("###### 02-STRING ######")
print("La asignatura de",asignatura,"Corresponde a la carrera de",carrera)

##Utilizando la funcion len(Cuenta la cantidad de caracteres)
print("La cantidad de caracteres de la palabara", asignatura, "es de:",len(asignatura),"\n")
print("La cantidad de caracteres de la palabara", carrera, "es de:",len(carrera),"\n")

##03 VALORES BOOLEANOS
ampolleta = False
interruptor = True

print("###### 03-BOOLEANS ######")
print("ampolleta,interruptor")
print("La variable ampolleta es de tipo",type(interruptor),"\n")#con type indicar el tipo de dato con el cual estamos trabajando

##Podemos transformar cualquier valor a un booelano ( al igual que un string, int, etc)
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
print(bool("\n"))

##04 Datos tipo list (Objetos de tipo coleccion) - (Mutables)
print("###### 04-LISTAS ######")

##Inicializando listas de 2 maneras
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacia:",nueva_lista)
print("Esta es otra lista vacia",otra_lista)
print(type(otra_lista))


estudiantes = ["Matias","Marco","Cristobal","Sebastian","Marco"]
num = [1,2,3,4,5,6,1]
lenguaje = ["Python"]

##¿se puede realizar una lista de datis compuestos?
data = ["Osorno",{"UV": "nivel bajo", "Temp °C":15}, (-40.5725, -73.1353)]
listamixta = ["Felipe", 100, True]
print("Lista de cadena de caracteres:",estudiantes)
print("Lista de numeros:",num)
print("Lista de un elemento:",lenguaje)
print("Esta es una lista mixta: ",listamixta)
print("Esto igual es una lista:",data)
print(len(listamixta))#para saber la cantidad de elementos de una lista 
print(estudiantes.count("Marco"))#Cantidad de ocurrencias de un elemento en la lista
print(num.count(1))

lenguaje = ["JavaScript"]
print("Nuevo valor del arreglo de un elemento:",lenguaje)

##¿Como accedo a un elemento especifico de la lista?
print(estudiantes[0])#correcto (1° elemento de la lista)
print(estudiantes[1])#(2° elemento de la lista)
#print(estudiantes[5]) #incorrecto
print("Posicion -2",estudiantes[-2])


##¿Que hacen estas funciones?
print(list("Python"))
print(list(range(1,3)))
print("\n")

## > en el fichero de listas se mostraran mas funciones

##TUPLAS - (no mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("###### 05-TUPLAS ######")
print(type(grupo1))

##Accediendo al primer elemento de la tupla
print(grupo1[0])

##Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite: ",grupo1.count ("Daniel"))

##Muestra el indice del primer elemento buscado
print("Indice del elemento:",grupo1.index ("Daniel"))

##Reasignando el primer elemento de la tupla
grupo1[0] = "Contanza"
print(grupo1)

##¿Se puede sumar las tuplas?

##Obteniendo un trozo de la tupa
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

##Entonces como no puedo modificar una tupla, que puede hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1,"\n"))
print("\n")

##06 - SETS (Conjuntos) - Estructura fija
#formas de inicializar un set
print("###### 06-SETS ######")
conjunto_vacio = set()
conjunto_vacio1 = {} ##¿diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set(["Azul","Rojo","Verde"]) #Utilizando la funcion set
conjunto_animales = {"gato","perro","Loro"} ##Utilizando corchetes

print(type(conjunto_colores)) #tipo de dato set
print(type(conjunto_animales))
print("El primer set contiene los siguientes colores: ",conjunto_colores)
print("El segundo set contiene los siguientes animales: ",conjunto_animales)

print(conjunto_animales[0])
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores)

##conjunto_animales.add("gato")
print("###### 07-DICCIONARIOS ######")
diccionarios = {}
datos_personales = {
    "Nombre":"Sebastian",
    "Institucion":"ulagos",
    "Edad":29,
    "Asignaturas":{"Estructura de Datos", "Programacion"}
}

print("Diccionario inicial:",datos_personales)

datos_personales["Institucion"] = "USS"
print("Diccionario actualizado: ",datos_personales)



