'''juntar vetores'''
# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
# compostos pelos elementos intercalados dos dois outros vetores.
num = []
num_two = []
num_three = []
for x in range(2):
    num.append(int(input('leia um numero: ')))
    num_two.append(int(input('leia um numero: ')))
    num_three.append(int(input('leia um numero: ')))
num.extend(num_two)
num.extend(num_three)
print(num)