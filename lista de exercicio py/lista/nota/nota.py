'''mostrar notas'''
# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o
# número de alunos com média maior ou igual a 7.0.
nota = []
cont = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
for x in range(3):
    n1 = float(input('digite a nota: '))
    n2 = float(input('digite a nota: '))
    n3 = float(input('digite a nota: '))
    n4 = float(input('digite a nota: '))
    nota.append((n1 + n2 + n3 + n4) / 4)
    if nota[x] >= 7:
        cont += 1
print(f'Alunos com notas maior igual a 7: {cont}')
