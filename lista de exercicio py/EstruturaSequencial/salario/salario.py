'''calcular salario'''
# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
horas = float(input("digite quantas  horas trabalhada: "))
while horas <= 0:
    horas = float(input("digite quantas  horas trabalhada: "))
valor = float(input("digite quanto voce ganha por hr: "))
while valor <= 0:
    valor = float(input("digite quanto voce ganha por hr: "))
print(f"salario bruto: {horas * valor}R$")
print(f"INSS: {(valor * horas) * 0.08}R$")
print(f"sindicato: {(valor * horas) * 0.05}R$")
print(f"salario liquido: {(horas * valor) * 0.86}R$")
