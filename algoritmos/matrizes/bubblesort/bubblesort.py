'''ordem alfabetica'''
# le 20 elementos e apresentar em ordem alfabetica
# entrada: nome[]
nome = []
for x in range(20):
    nome.append((input("digite um nome: ")))
for x in range(20):
    for j in range(x + 1, 5, 1):
        if nome[x] > nome[j]:
            nome[x], nome[j] = nome[j], nome[x]
for x in range(20):
    print(nome[x])
