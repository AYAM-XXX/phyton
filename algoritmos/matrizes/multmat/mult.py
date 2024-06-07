vetA = []
vetB = []
matriz = []
for x in range(12):
    vetA.append(int(input("insira um numero vetA: ")))
    vetB.append(int(input("insira um numero vetB: ")))
for x in range(2):
    linha = []
    for y in range(12):
        if x == 0:
            linha.append(vetA[y] * 2)
        else:
            linha.append(vetB[y] - 5)
    matriz.append(linha)
print(matriz)
