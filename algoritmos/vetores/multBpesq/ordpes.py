'''multiplica e pesquisar'''
# ler 8 elementos de uma matriz A tipo vetor.construir uma matriz B
# de mesma dimensão com os elementos multiplicados por 5
# apresentar a matriz B uma ordem crescente e um mecanismo de pesquisa
# entrada: vetA[], vetB[]
# saida: mostrar ordenado, mecanismo de pesquisa
vetA = []
vetB = []
for x in range(8):
    vetA.append(int(input("digite o numero: ")))
    vetB.append(vetA[x] * 5)
for x in range(8):
    for z in range(x + 1, 8):
        if vetB[x] > vetB[z]:
            vetB[x], vetB[z] = vetB[z], vetB[x]
for x, item in enumerate(vetB):
    print(item)
cond = input("'s' para pesquisar item\n'n' para encerrar\ndigite: ")
cond.lower()
while cond != 's' and cond != 'n':
    cond = input("'s' para pesquisar item\n'n' para encerrar\ndigite: ")
    cond.lower()
while cond == 's':
    pesq = int(input("\nsearch: "))
    if pesq in vetB:
        ind = vetB.index(pesq)
        print(f'-----\n{pesq} está na lista no indice {ind}\n-----')
    else:
        print("------\nitem não esta na lista\n------")
    cond = input("\n's'continuar\n'n' encerrar\ndigite: ")
    while cond != 's' and cond != 'n':
        cond = input("\n's' continuar\n'n' encerrar\ndigite: ")
