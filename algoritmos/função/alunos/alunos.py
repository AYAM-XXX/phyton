'''alunos'''
# cadastrar 20 alunos, classificar notas, corrigir notas,
# alunos aprovados e reprovados
alunos = []
tam = 1


def cadastro(matrizcad):
    for x in range(tam):
        lista = []
        soma = 0
        media = 0
        for y in range(4):
            if y == 0:
                inf = input("digite o nome: ")
                lista.append(inf)
            elif y > 0 and y < 4:
                inf = float(input(f"digite a nota do {y} bimestre: "))
                while inf < 0 or inf > 10:
                    inf = float(input(f"digite a nota do {y} bimestre: "))
                lista.append(inf)
                soma += inf
        media = float(soma) / 3
        lista.append(media)
        matrizcad.append(lista)


def ranking(matriz):
    for x in range(tam):
        for y in range(tam):
            if matriz[x][4] > matriz[y][4]:
                matriz[x], matriz[y] = matriz[y], matriz[x]
    print("\nRanking das melhores notas\n")
    for x in range(tam):
        print(f"{x + 1}° lugar {matriz[x][0]}| media: {matriz[x][4]:.2f}")


def corrigir(id, matriz):
    soma = 0
    media = 0
    for y in range(4):
        if y == 0:
            inf = input("digite o nome: ")
            matriz[id][y] = inf
        elif y > 0 and y < 4:
            inf = float(input(f"digite a nota do {y} bimestre: "))
            soma += float(inf)
            matriz[id][y] = inf
    media = float(soma) / 3
    matriz[id][y] = media
    print(matriz[id])


def pesquisar(id, matriz):
    print("\nresultado da pesquisa\n")
    for x in range(5):
        if x == 0:
            print(f"\nnome: {matriz[id][x]}")
        elif x > 0 and x < 4:
            print(f"\n{x}° bimestre nota: {matriz[id][x]}")
        else:
            print(f"\nmedia: {matriz[id][x]}")


def aprovados(matriz):
    print("\nlista de aprovados\n")
    for x in range(tam):
        if matriz[x][4] >= 6:
            print(f"{matriz[x][0]}\n")


def reprovados(matriz):
    print("\nlista de reprovados\n")
    for x in range(tam):
        if matriz[x][4] < 6:
            print(f"{matriz[x][0]}\n")


cadastro(alunos)
print("<---------MENU--------->\n")
print("1- ranking\n")
print("2- pesquisar\n")
print("3- corrigir dados\n")
print("4- aprovados\n")
print("5- reprovados\n")
print("6- fim\n")
print("<---------------------->\n")
seach = int(input("digite sua escolha: "))
while seach < 1 or seach > 6:
    seach = int(input("digite sua escolha: "))
while seach != 6:
    if seach == 1:
        ranking(alunos)
    elif seach == 2:
        id = (int(input("\ndigite o codigo do aluno: ")))
        while id < 0 or id > tam:
            id = (int(input("\ndigite o codigo do aluno: ")))
        pesquisar(id, alunos)
    elif seach == 3:
        id = (int(input("\ndigite o codigo do aluno: ")))
        while id < 0 or id > tam:
            id = (int(input("\ndigite o codigo do aluno: ")))
        corrigir(id, alunos)
    elif seach == 4:
        aprovados(alunos)
    else:
        reprovados(alunos)
    print("<---------MENU--------->\n")
    print("1- ranking\n")
    print("2- pesquisar\n")
    print("3- corrigir dados\n")
    print("4- aprovados\n")
    print("5- reprovados\n")
    print("6- fim\n")
    print("<---------------------->\n")
    seach = int(input("digite sua escolha: "))
    while seach < 1 or seach > 6:
        seach = int(input("digite sua escolha: "))
