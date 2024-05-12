'''nota  de alunos'''
# criar um progama que pega a nota e nome dos alunos , calcula a media
# para os alunos acima da media ele da uma msg de parabens
# entrada: nome[], nota[], media, nmralunos
# saida: nome do aluno com parabens
import os
NmrAlunos = int(input("qual o numero de alunos: "))
while NmrAlunos < 1:
    NmrAlunos = int(input("qual o numero de alunos: "))
nome = []
nota = []
media = 0

for x in range(NmrAlunos):
    nome.append(input("nome do aluno: "))
    nt = 0
    soma = 0
    for i in range(3):
        nt = float(input(f"digite a nota [{i + 1}]: "))
        while nt < 0:
            nt = float(input(f"digite a nota [{i + 1}]: "))
        soma = float(soma) + nt
    nota.append(soma / 3)
    if nota[x] < 6:
        recp = float(input("nota de recuperação: "))
        while recp < 0 or recp > 10:
            recp = float(input("nota de recuperação: "))
        nota[x] = (nota[x] + recp) / 2
    media = media + nota[x]
media = media / NmrAlunos
os.system('cls')
for x in range(NmrAlunos):
    if nota[x] > 6 and nota[x] > media:
        print("-------------------------------------")
        print(f"aluno: {nome[x]}\nnota: {nota[x]:.2f}\nsituação: aprovado")
        print("parabens, você está acima da media")
        print("-------------------------------------")
    elif nota[x] >= 6:
        print("-------------------------------------")
        print(f"aluno: {nome[x]}\nnota: {nota[x]:.2f}\nsituação: aprovado")
        print("-------------------------------------")
    else:
        print("-------------------------------------")
        print(f"aluno: {nome[x]}\nnota: {nota[x]:.2f}\nsituação: reprovado")
        print("-------------------------------------")
print(f"media da turma: {media:.2f}")
