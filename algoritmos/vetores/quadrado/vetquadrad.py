'''quadrado vetor'''
# criar uma matriz de 20 elementos e todo elemento que a matriz A tiver a B
# vai ser o quadrado desse elemento
vetA = []
vetB = []

for x in range(20):
    vetA.append(int(input("digite um valor: ")))
    vetB.append(vetA[x]**2)
print(vetA)
print(vetB)
