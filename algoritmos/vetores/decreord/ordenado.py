'''ordena elementos modo decrescente'''
# ordenar 12 elementos de uma mtriz tipo vetor, colocalos
# na ordem decrescente e apresentar os elementos ordenados
# entrada: vet[]
vet = []
for x in range(12):
    vet.append(input("digite o nome: "))
    vet[x].lower()
for x in range(12):
    for z in range(x + 1, 12):
        if vet[x] < vet[z]:
            vet[x], vet[z] = vet[z], vet[x]
for x, item in enumerate(vet):
    print(item)
