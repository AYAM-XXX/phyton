'''pesquisa elementos dentro de uma matriz'''
# ler 10 elementos e procuras eles na matriz
nome = []
for x in range(10):
    nome.append(input("digite o nome: "))
    nome[x].lower()
key = 'S'
while key == 'S':
    pes = input("digite o nome que está procurando: ")
    if pes in nome:
        indice = nome.index(pes)
        print(f'{pes}, esta na lista no indice: {indice}')
    else:
        print(f'{pes} não esta na lista')
    key = input("S - para continuar procurando\nN - para parar\ndigite: ")
    while key != 'S' and key != 'N':
        key = input("S - para continuar procurando\nN - para parar\ndigite: ")
# acha = 0
# for x in range(10):
#     if pes == nome[x]:
#         acha = 1

# if acha == 1:
#     print(f'{pes}, foi encontrado')
# else:
#     print(f'{pes}, não foi encontrado')
