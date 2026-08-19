'''calcular peso ideal'''
# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
sexo = input("digite seu sexo: ")
while sexo != 'mulher' and sexo != "homem":
    sexo = input("digite seu sexo: ")
altura = float(input("digite sua altura: "))
while altura <= 0:
    altura = float(input("digite sua altura: "))
if sexo == "homem":
    print(f"seu peso ideal: {(72.7 * altura) - 58}")
else:
    print(f"seu peso ideal: {(62.1 * altura) - 44.7}")
