##para comentar alooooo alooooo

print("ola ")

#01 declarando variables

##variable estilo String(texto)
nombre= "sebastian"
name= "kharoll"

##02 impresion de una variable
print(nombre)
print("Hola soy", nombre)

print(name)
print("Hola soy", name)

##03 Declarando variable de tipo numerico
## int(enteros)
## float(decimales)
## complex(complejo)
edad = 18
print("hola mi edad es: ",edad)

##04 Imprimiendo 2 variables en una misma linea

print("Hola mi nombre es: ",nombre,"y tengo:",edad, "años")##Impresion separando con comas
print("Hola mi nombre es"," "+name+" "+"y tengo"+" "+str(edad)+" "+"años")##Concatenar con signo +
print(f"hola mi nombre es {nombre} y tengo {edad} años")##formato de cadenas literales 

##05 Actualizando la variable nombre (mutable)
nombre= "Samantha"
print("Hola mi nuevo nombre es:",nombre)

##06 Variables en una sola linea ( no es muy recomendable, solo en ciertas situaciones)
ciudad, region, pais, year = " Puerto Montt", "Los lagos", "Chile", 2010
print("Yo naci en la ciudad de",ciudad, ",en la region de",region,"en el pais de",pais,"en el año ",year)


##07 Utilizando la intruccion INPUT

nombre1=input("¿Cual es tu nombre?\n")##\n para hacer un salto en linea
edad1=input("'¿Cual es tu edad?\n")
print("Tu nombre es:",nombre1,"y tu edad es:",edad)