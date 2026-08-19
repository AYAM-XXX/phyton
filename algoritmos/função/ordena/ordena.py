'''ordenação de codigo'''
# ordena um vetor em função
vetor = []
tam = 5


def ordena(org):
    for x in range(len(vetor)):
        for y in range(len(vetor)):
            if org[x] < org[y]:
                org[x], org[y] = org[y], org[x]


for x in range(tam):
    inf = int(input("preencha o vetor: "))
    vetor.append(inf)
ordena(vetor)
print(vetor)
