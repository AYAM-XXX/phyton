'''calcular raio'''
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("digite o raio: "))
while raio <= 0:
    raio = float(input("digite o raio: "))
print(f"area: {3.14 * (raio ** 2)}")
