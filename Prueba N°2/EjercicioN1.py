divisibles5=[]
impares=[]
for numero in range(2,30,3):
    print(numero)
    if numero%5==0:
        divisibles5.append(numero)
    if numero%2!=0:
        impares.append(numero)
print("Los numeros divisibles por 5 son:",divisibles5)
print("su suma es:",sum(divisibles5))
print("Los numeron inpares son:",impares,"su suma es:",sum(impares))