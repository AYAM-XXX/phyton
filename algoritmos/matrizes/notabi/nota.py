'''nota aluno'''
# realizar um pograma que em uma matriz recebe a nota de 4 bimestre
# e o nome do aluno, e organize em oredem alfabetica e faça a media
notas = []
soma = 0
for x in range(8):
    dados = []
    for y in range(5):
        if y == 0:
            dados.append(input("digite o nome:"))
        elif y == 1:
            nota = float(input(f"digite nota do {y}° bim: "))
            while nota < 0:
                nota = float(input(f"digite nota do {y}° bim: "))
            dados.append(nota)
            soma += dados[y]
        elif y == 2:
            nota = float(input(f"digite nota do {y}° bim: "))
            while nota < 0:
                nota = float(input(f"digite nota do {y}° bim: "))
            dados.append(nota)
            soma += dados[y]
        elif y == 3:
            dnota = float(input(f"digite nota do {y}° bim: "))
            while nota < 0:
                nota = float(input(f"digite nota do {y}° bim: "))
            dados.append(nota)
            soma += dados[y]
        elif y == 4:
            nota = float(input(f"digite nota do {y}° bim: "))
            while nota < 0:
                nota = float(input(f"digite nota do {y}° bim: "))
            dados.append(nota)
            soma += dados[y]
    notas.append(dados)
for x in range(8):
    for y in range(8):
        if notas[x][0] < notas[y][0]:
            notas[x][0], notas[y][0] = notas[y][0], notas[x][0]
for x in range(8):
    for y in range(5):
        if y == 0:
            print("/------------------/")
            print(f" |nome: {notas[x][y]}|\n ---------------")
        elif y == 1:
            print(f" {y}° semestre\n    nota: {notas[x][y]}\n ---------------")
        elif y == 2:
            print(f" {y}° semestre\n    nota: {notas[x][y]}\n ---------------")
        elif y == 3:
            print(f" {y}° semestre\n    nota: {notas[x][y]}\n ---------------")
        elif y == 4:
            print(f" {y}° semestre\n    nota: {notas[x][y]}\n ---------------")
print(f"media geral: {soma/32}")
