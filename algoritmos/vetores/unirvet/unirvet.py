'''união de vetores'''
# ler 2 A e B vetores com 15 elementos cada e unir em um vetor C
# entrada: vetA[], vetB[], vetC[]
vetA = []
vetB = []
vetC = []
for x in range(15):
    vetA.append(int(input("vetA digite um valor: ")))
    vetB.append(int(input("vetB digite um valor: ")))
    vetC.append(vetA[x])
    vetC.append(vetB[x])
for x, item in enumerate(vetC):
    print(item)
