salario = float(input("insira o salario: "))
if(salario > 4000):
    print(f"salario: {(salario * 0.725):.2f}")
elif (salario <= 4000 and salario <= 2500):
    print(f"salario: {(salario * 0.85):.2f}")
else:
    print("isento")










# Cálculo de Imposto Progressivo: Peça o salário de um desenvolvedor júnior. Se for maior que R$4000.00
# exiba o desconto de 27.5% de imposto. Se for entre R$2500.00 e R$4000.00, aplique 15%. Abaixo disso,
# exiba "Isento".