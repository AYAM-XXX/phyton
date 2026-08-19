numeros = []
positivos = []
negativos = []
for x in range(0, 5):
    num = int(input("digite o numero: "))
    if num > 0:
        positivos.append(num)
        numeros.append(num)
    else:
        negativos.append(num)
        numeros.append(num)


print(positivos)
print(negativos)
print(numeros)