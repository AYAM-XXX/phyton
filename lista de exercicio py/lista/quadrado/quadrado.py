'''quadrado do numero da lista '''
# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.
num = []
for x in range(10):
    valr = int(input("digite um valor: "))
    num.append(valr ** 2)
print(num)