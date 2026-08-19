'''conversor'''
# Faça um Programa que converta metros para centímetros
metros = float(input("digite o valor em metros: "))
while metros <= 0:
    metros = float(input("digite o valor em metros: "))
print(f"{metros * 100}cm")
