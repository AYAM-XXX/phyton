'''inversor de vetores'''
# ler 20 elementos e colocar de ordem trocada em outro

vetA = []
vetB = []
cont = 0
for x in range(3):
    vetA.append(int(input("digite um numero: ")))
vetB = vetA[:: - 1]
print(vetA)
print(vetB)
