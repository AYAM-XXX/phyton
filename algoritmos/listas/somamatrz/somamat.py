'''soma 2 matrizes'''
# ler 2 matrizes de 5 linhas e 3 colunas e soma os valores das duas e colocar
# em uma matriz diferente
matA = []
matB = []
matC = []
for x in range(5):
    linhaA = []
    linhaB = []
    for y in range(3):
        linhaA.append(int(input("insira um valor para matriz A: ")))
        linhaB.append(int(input("insira um valor para matriz B: ")))
    matA.append(linhaA)
    matB.append(linhaB)
for x in range(5):
    linhaC = []
    for y in range(3):
        linhaC.append(matA[x][y] + matB[x][y])
    matC.append(linhaC)
print(f"matriz A: \n{matA}\n")
print(f"matriz B: \n{matB}\n")
print(f"matriz C: \n{matC}\n")
