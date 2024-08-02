'''Valida e corrige número de telefone'''
# Faça um programa que leia um número de telefone, e corrija
# o número no caso deste conter somente 7 dígitos, acrescentando
# o '3' na frente. O usuário pode informar o número com ou sem o 
# traço separador.

nmr = input("digite o numero: ")
while len(nmr) != 7:
    nmr = input("digite o numero: ")
if nmr[0] != 3:
    nmr = '3' + nmr[0:7 + 1]
if '-' not in nmr:
    nmr = nmr[0:4] + '-' + nmr[4:7 + 1]
print(nmr)