"uma mamtriz com nome e idade"
# prenche uma matriz com nome e idade da pessoa
pessoas = []
for i in range(2):
    nome = input('digite o nome: ')
    idade = input('digite a idade: ')
    pessoas.append([nome, idade])
menor = 0
for i in range(len(pessoas)): 
    if pessoas[i][1] < pessoas[menor][1]:
        menor = i
print(pessoas)
print(f"menor idade: {pessoas[menor][1]}")
