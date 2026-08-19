'''soma e multiplica vetor'''
# Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.
num = []
mult = 1
soma = 0
for x in range(5):
    num.append(int(input("digite um numero: ")))
    soma += num[x]
    mult = mult * num[x]
print(f'soma: {soma}\nmult: {mult}')