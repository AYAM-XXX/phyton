''' reajuste salario'''
# As Organizações Tabajara resolveram dar um aumento de salário
# segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento
# ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento
salario = float(input("digite o salario: "))
if salario <= 280:
    print(f"salario antigo: {salario}\ntaxa de aumento: 20%")
    print(f"valor do aumento: {salario * 0.20:.2f}")
    print(f"novo salario: {salario * 1.20}")
elif salario > 280 and salario <= 700:
    print(f"salario antigo: {salario}\ntaxa de aumento: 15%")
    print(f"valor do aumento: {salario * 0.15:.2f}")
    print(f"novo salario: {salario * 1.15}")
elif salario > 700 and salario <= 1500:
    print(f"salario antigo: {salario}\ntaxa de aumento: 10%")
    print(f"valor do aumento: {salario * 0.10:.2f}")
    print(f"novo salario: {salario * 1.10}")
elif salario > 1500:
    print(f"salario antigo: {salario}\ntaxa de aumento: 10%")
    print(f"valor do aumento: {salario * 0.05:.2f}")
    print(f"novo salario: {salario * 1.05}")
else:
    print("valor invalido")
