'''contabliziar pares e impares'''
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.
num = []
par = []
imp = []
for x in range(20):
    num.append(int(input('digite um numero: ')))
    if num[x] % 2 == 0:
        par.append(num[x])
    else:
        imp.append(num[x])
print(f'numeros: {num}\npares: {par}\nimpares: {imp}')
