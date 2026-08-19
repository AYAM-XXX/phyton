'''pesquisa elementos dentro de uma matriz'''
# ler 10 elementos e procuras eles na matriz
nome = []
for x in range(10):
    nome.append(input("digite o nome: "))
    nome[x].lower()
key = input("S - pesquisar item\nN - sair\nDigite: ")
while key != "S" and key != "N":
    key = input("S - pesquisar item\nN - sair\nDigite: ")
while key == 'S':
    pes = input("\ndigite o nome que está procurando: ")
    if pes in nome:
        indice = nome.index(pes)
        print(f'\n===\n{pes}, esta na lista no indice: {indice}\n===\n')
    else:
        print(f'\n===\n{pes} não esta na lista\n===\n')
    key = input("\nS - para continuar procurando\nN - finalizar\ndigite: ")
    while key != 'S' and key != 'N':
        key = input("\nS - para continuar procurando\nN - finalizar\ndigite: ")
# acha = 0
# for x in range(10):
#     if pes == nome[x]:
#         acha = 1

# if acha == 1:
#     print(f'{pes}, foi encontrado')
# else:
#     print(f'{pes}, não foi encontrado')
