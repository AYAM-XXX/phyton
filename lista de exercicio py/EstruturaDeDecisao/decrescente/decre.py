'''colocar em ordem decrecente'''
# Faça um Programa que leia três números e mostre-os em ordem
# decrescente
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"decrescente: {n1}, {n2}, {n3}")
    else:
        print(f"decrescente: {n1}, {n3}, {n2}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"decrescente: {n2}, {n1}, {n3}")
    else:
        print(f"decrescente: {n2}, {n3}, {n1}")
else:
    if n2 > n1:
        print(f"decrescente: {n3}, {n2}, {n1}")
    else:
        print(f"decrescente: {n3}, {n1}, {n2}")
