'''altura dos alunos'''
# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
# determine quantos alunos com mais de 13 anos possuem altura inferior à 
# média de altura desses alunos.
altura = []
idade = []
const = 3
cont = 0
total = 0
for x in range(3):
    altura.append(float(input("digite a altura: ")))
    idade.append(int(input("digite a idade: ")))
    total += altura[x]
    media = total / const
    if altura[x] < media and idade[x] >= 13:
        cont += 1
print(f'alunos com mais de 13 anos possuem altura inferior à média: {cont}')