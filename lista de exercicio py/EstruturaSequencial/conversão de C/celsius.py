'''calcular quadrado'''
# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

# Faça um Programa que peça a temperatura em graus Celsius,
#  transforme e mostre em graus Fahrenheit.
# (C × 9/5) + 32
Fahrenheit = float(input("digite quantos graus Fahrenheit: "))
print(f"celsius: {5 * ((Fahrenheit - 32) / 9):.1f}c°")

celsius = float(input("digite quantos graus celsius: "))
print(f"Fahrenheit: {(celsius * 9/5) + 32}f°")
