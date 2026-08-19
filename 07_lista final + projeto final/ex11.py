numeros = (26, 49, 4, 29, 36, 79, 26, 89, 80, 8)
cont_par = 0
cont_impar = 0

for x in range(0, 10):
    if numeros[x] % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"numeros pares: {cont_par}\nnumeros impares: {cont_impar}")
