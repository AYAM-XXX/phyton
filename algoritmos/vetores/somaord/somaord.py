'''somar vetores diferentes e ordenar'''
# ler 12 elementos de um vet A B ordenar eles e somar em um vet C
# e ordenar e decrecesnte
vetA = []
vetB = []
vetC = []
for x in range(12):
    vetA.append(int(input("digite um numero [vetA]: ")))
for x in range(12):
    vetB.append(int(input("digite um numero [vetB]: ")))
for x in range(12):
    for z in range(12):
        if vetA[x] < vetA[z]:
            vetA[x], vetA[z] = vetA[z], vetA[x]
        if vetB[x] < vetB[z]:
            vetB[x], vetB[z] = vetB[z], vetB[x]
for x in range(12):
    vetC.append(vetA[x] + vetB[x])
for x in range(12):
    for z in range(12):
        if vetC[x] > vetC[z]:
            vetC[x], vetC[z] = vetC[z], vetC[x]
print("vetA")
for x, item in enumerate(vetA):
    print(item)
print("vetB")
for x, item in enumerate(vetB):
    print(item)
print("vetC")
for x, item in enumerate(vetC):
    print(item)
