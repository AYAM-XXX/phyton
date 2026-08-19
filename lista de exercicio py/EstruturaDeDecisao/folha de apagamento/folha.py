'''folha de pagamento'''
# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
# abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
# ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da
# sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as
# informações, dispostas conforme o exemplo abaixo. No exemplo o valor da
# hora é 5 e a quantidade de hora é 220.
horas = int(input("digite as horas trabalhadas: "))
valor_hora = float(input("digite o valor da hora: "))
salario = horas * valor_hora
sind = 0.3
fgts = 0.11
if salario <= 900:
    print(f"salario: R$ {salario}")
    print("IR: isento")
    print(f"INSS: R$ {salario * 0.10}")
    print(f"FGTS: R$ {salario * 0.11}")
    print(f"sindicato: R$ {salario * 0.03}")
    print(f"total descontos: R$ {salario * 0.13}")
    print(f"salario liquido: R$ {salario * 0.87}")
elif salario > 900 and salario <= 1500:
    print(f"salario: R$ {salario}")
    print(f"IR: R$ {salario * 0.05}")
    print(f"INSS: R$ {salario * 0.10}")
    print(f"FGTS: R$ {salario * 0.11}")
    print(f"sindicato: R$ {salario * 0.03}")
    print(f"total descontos: R$ {salario * 0.18}")
    print(f"salario liquido: R$ {salario * 0.82}")
elif salario > 1500 and salario <= 2500:
    print(f"salario: R$ {salario}")
    print(f"IR: R$ {salario * 0.10}")
    print(f"INSS: R$ {salario * 0.10}")
    print(f"FGTS: R$ {salario * 0.11}")
    print(f"sindicato: R$ {salario * 0.03}")
    print(f"total descontos: R$ {salario * 0.28}")
    print(f"salario liquido: R$ {salario * 0.72}")
elif salario > 2500:
    print(f"salario bruto: R$ {salario}")
    print(f"IR: R$ {salario * 0.20}")
    print(f"INSS: R$ {salario * 0.10}")
    print(f"FGTS: R$ {salario * 0.11}")
    print(f"sindicato: R$ {salario * 0.03}")
    print(f"total descontos: R$ {salario * 0.38}")
    print(f"salario liquido: R$ {salario * 0.62}")
else:
    print("valor incorreto")
