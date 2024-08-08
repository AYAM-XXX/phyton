'''Guarda dados de pessoas'''
# Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. Imprima a idade
#  e a altura na ordem inversa a ordem lida.
idade = []
altura = []
for x in range(5):
    idade.append(int(input(f"pessoa {x} digite a idade: ")))
    altura.append(float(input(f"pessoa {x} digite a altura: ")))
for x in range(2, 0, -1):
    print(f'idade: {idade[x]}')
    print(f'altura: {altura[x]}')
