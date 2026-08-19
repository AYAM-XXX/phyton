"""unir matrizes"""
# ler 2 vetores e unir em uma matriz sendo que o vetor A onde a
# primeira coluna e a matriz A e a segunda coluna e matriz B
vetA = []
vetB = []
matC = []
for x in range(7):
    vetA.append(int(input("digite valor vet A: ")))
    vetB.append(int(input("digite valor vet B: ")))
for x in range(2):
    linhaC = []
    for y in range(7):
        if x == 0:
            linhaC.append(vetA[y])
        else:
            linhaC.append(vetB[y])
    matC.append(linhaC)
print(f"vet A:\n{vetA}\n")
print(f"vet B:\n{vetB}\n")
print(f"mat:\n{matC}\n")
