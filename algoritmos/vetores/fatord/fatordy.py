'''fatorial e ordenação'''
# ler um vetor A com 15 elementos e criar um vetor B do mesmo tipo
# so que cada elemento e um fatorial e depois ordernar de forma crescente
vetA = []
vetB = []
for x in range(15):
    vetA.append(int(input("digite um numero: ")))
    soma = 1
    for i in range(vetA[x]):
        soma = soma * (i + 1)
    vetB.append(soma)
for x in range(15):
    for z in range(15):
        if vetB[x] > vetB[z]:
            vetB[x], vetB[z] = vetB[z], vetB[x]
for x, item in enumerate(vetB):
    print(item)
