# Lista revisão Python
# 1. Faça um programa que mostre todos os números de 1 a 100 e indique ao lado se
# o número é par ou ímpar.

for x in range(1, 101):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
