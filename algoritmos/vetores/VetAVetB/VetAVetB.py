'''valor de matrizes'''
# fazer um progama que le 10 elementos de um vetor A  depois
# depois fazer uma matriz B do mesmo tipo sendo que se
# o indice for par o valor deve ser multiplicado por 5
# indice impar deve soma + 5 no valor
# entrada: vetorA[], vetorB[]
vetA = []
vetB = []
for x in range(10):
    vetA.append(int(input("digite o valor: ")))
    if x % 2 == 0:
        vetB.append(vetA[x] * 5)
    else:
        vetB.append(vetA[x] + 5)
for x in range(10):
    print(f"vetor A[{x}]: {vetA[x]}    vetor B[{x}]: {vetB[x]}")
