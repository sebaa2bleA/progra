MinimoDeNotas = 10
sumnotas = 0
contadorDenotas = 0
notasAltas = 0
notasBajas = 0


while contadorDenotas < MinimoDeNotas:
    nota = float(input("Ingrese un total de 10 notas entre 1.0 y 7.0): "))
    if nota >= 1.0 and nota <= 7.0:
        sumnotas += nota
        contadorDenotas += 1
        if nota > (sumnotas / contadorDenotas):
            notasAltas += 1
        elif nota < (sumnotas/ contadorDenotas):
            notasBajas += 1
    else:
        print("Nota equivocada, Debe ingresar una nota valida entre el 1.0 y el 7.0")

media = sumnotas / contadorDenotas


print("La media de las calificaciones es:", media)
print("Número de calificaciones más altas que la media:", notasAltas)
print("Número de calificaciones más bajas que la media:", notasBajas)
