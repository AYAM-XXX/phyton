"""fatorial"""
# criar uma matriz A com 15 elementos e outra matriz B com a fatorial
# entrad: matrizA[], matrizB[], fat
vetA = []
vetB = []
for x in range(15):
    vetA.append(int(input("digite o numero: ")))
for x in range(15):
    soma = 1
    for i in range(vetA[x]):
        soma = soma * (i + 1)
    vetB.append(soma)
for x, item in enumerate(vetA):
    print(item)
for x, item in enumerate(vetB):
    print(item)
