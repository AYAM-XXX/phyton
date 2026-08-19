# 2.Desenvolva um sistema básico que leia números inteiros fornecidos pelo usuário e
# conte quantos números digitados eram pares. O loop encerra quando o usuário digitar
# o número 0.

num = -1
cont = 0
while num != 0:
    num  = int(input("Enter a number: "))
    if(num % 2 == 0):
        cont += 1
print(cont)   