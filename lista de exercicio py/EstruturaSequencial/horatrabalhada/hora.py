'''calcular quadrado'''
# Faça um Programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre o total do seu
# salário no referido mês.
horas = float(input("digite quantas  horas trabalhada: "))
while horas <= 0:
    horas = float(input("digite quantas  horas trabalhada: "))
valor = float(input("digite quanto voce ganha por hr: "))
while valor <= 0:
    valor = float(input("digite quanto voce ganha por hr: "))
print(f"salario: {(horas * valor)}")
