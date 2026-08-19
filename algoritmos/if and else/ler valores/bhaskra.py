'''segundo gral'''
import math
# ler 3 valres e fazer uma equação do segundo grau
valor1 = float(input("digite o valor: "))
valor2 = float(input("digite o valor: "))
valor3 = float(input("digite o valor: "))
delta = valor2**2 - (4 * (valor3 * valor1))
raiz1 = ((-1 * (valor2)) + math.sqrt(delta)) / (2*valor1)
raiz2 = ((-1 * (valor2)) - math.sqrt(delta)) / (2*valor1)
print(f"primeira raiz: {raiz1:.2f}")
print(f"primeira raiz: {raiz2:.2f}")
