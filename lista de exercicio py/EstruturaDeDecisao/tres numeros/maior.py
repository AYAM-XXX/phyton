'''msotra o maior de tres numeros'''
# Faça um Programa que leia três números e mostre o maior deles
# e menor deles
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))
if n1 > n2 and n1 > n3:
    print(f"maior  numero: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"maior  numero:  {n2}")
else:
    print(f"maior  numero: {n3}")
if n1 < n2 and n1 < n3:
    print(f"menor  numero: {n1}")
elif n2 < n1 and n2 < n3:
    print(f"menor  numero:  {n2}")
else:
    print(f"menor  numero: {n3}")
