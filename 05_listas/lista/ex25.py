# 25. (Almoxarifado): Uma lista de contagem de caixas possui valores positivos, nulos e
# negativos (erros de digitação): [15, -3, 0, 22, -1, 8]. Construa um programa
# que conte e mostre quantos valores válidos (maiores que zero) existem na lista.

nums = [15, -3, 0, 22, -1, 8]
cont = 0
for num in nums:
    if num > 0:
        print(num)
        cont += 1

print(f"numeros maiores que 0: {cont}")
