'''calcular numeros'''
# Faça um Programa que peça 2 números inteiros e um número real
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input("leia o primeiro numero: "))
n2 = int(input("leia o segundo numero: "))
n3 = int(input("leia o terceiro numero: "))
print(f"resultado letra A: {(n1 * 2) * (n2 / 2)}")
print(f"resultado letra B: {(n1 * 3) + n3}")
print(f"resultado letra C: {(n3 ** 3)}")
