from os import system
system("cls")
nombre=input("Ingrese el nombre del estudiante: ")
asignatura=input("Ingrese el nombre de la asignatura: ")
nota1=float(input("Ingrese la nota N°1 del estudiante: "))
nota2=float(input("Ingrese la nota N°2 del estudiante: "))
prom1=(nota1*0.3)
prom2=(nota2*0.7)
promtotal=prom1+prom2
Datos_personales = {
    "Nombre":nombre,
    "Asignatura":asignatura,
    "Nota 1":nota1,
    "Nota 2":nota2,
    "Promedio Ponderado":f"{promtotal:.1f}"}
print("Diccionario inicial:",Datos_personales)