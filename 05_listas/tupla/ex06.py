# 6. Filtrando Pares
# Escreva um programa que receba uma tupla com 10 números inteiros quaisquer.
# O programa deve gerar uma nova tupla contendo apenas os números pares da
# tupla original.

numeros = (12, 45, 7, 23, 89, 54, 2, 31, 76, 18)

pares = []

for x in range(len(numeros)):
    if numeros[x] % 2 == 0:
        pares.append(numeros[x])

tupla_pares = (pares)
print(tupla_pares)