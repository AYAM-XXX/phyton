"matriz com fatorial"
# criar um vetor e a aprte de cima da matriz e Esse vetor + 5 em cada elementos
# a segunda coluna e o fatorial desse vetor
# o segundo e o quadrado de cada numero
vet = []
matriz = []
for x in range(10):
    vet.append(int(input("insira um numero: ")))
for x in range(3):
    linha = []
    for y in range(10):
        if x == 0:
            linha.append(vet[y] + 5)
        elif x == 1:
            for u in range(10):
                fat = 1
                for z in range(vet[u]):
                    fat = fat * (z + 1)
                linha.append(fat)
        else:
            linha.append(vet[y]**2)
    matriz.append(linha)
print(matriz)
