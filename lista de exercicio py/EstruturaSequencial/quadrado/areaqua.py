'''calcular quadrado'''
# Faça um Programa que calcule a área de um quadrado,em seguida
# mostre o dobro desta área para o usuário.
lado = float(input("digite o lado: "))
while lado <= 0:
    lado = float(input("digite o raio: "))
print(f"area em dobro: {(lado * lado) * 2}")
