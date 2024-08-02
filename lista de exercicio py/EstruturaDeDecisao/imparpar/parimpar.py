'''define se um numero e impar ou par'''
# Faça um Programa que peça um número inteiro e determine
# se ele é par ou impar.
nmr = int(input("digite um numero: "))
if nmr % 2 != 0:
    print(f"{nmr} e impar ")
else:
    print(f"{nmr} e par ")
