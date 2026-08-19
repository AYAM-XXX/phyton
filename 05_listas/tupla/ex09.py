# 9. Boletim Simples
# Crie um programa que armazene o nome de 3 alunos e suas respectivas notas em
# uma tupla de tuplas, no formato: ((Nome1, Nota1), (Nome2, Nota2), (Nome3,
# Nota3)). Varra essa estrutura e exiba o nome de cada aluno e se ele foi "Aprovado"
# (nota >= 7) ou "Reprovado" (nota < 7).

alunos_notas = (
    ("Ana", 8.5),
    ("Bruno", 6.0),
    ("Carlos", 9.2)
)


for x in range(len(alunos_notas)):
    for y in range(0, 2):
        if(y == 1):
            if(alunos_notas[x][y] >= 7):
                print(f"aluno: {alunos_notas[x][y-1]}\nnota: {alunos_notas[x][y]}\nsituação: aprovado\n")
            elif(alunos_notas[x][y] < 7):
                print(f"aluno: {alunos_notas[x][y-1]}\nnota: {alunos_notas[x][y]}\nsituação: reprovado\n")
