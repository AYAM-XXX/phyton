'''lista de numero inveso'''
# Faça um Programa que leia um vetor de 10 números reais e
# mostre-os na ordem inversa
num = []
for x in range(10):
    num.append(int(input('digite um numero: ')))
num.sort(reverse=True)
print(num)
