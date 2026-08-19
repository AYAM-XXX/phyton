valor_carro = float(input("insira o valor do carro: "))
salario = float(input("insira o valor do salario: "))
meses = int(input("insira a quantidade de meses: "))
if( (meses / valor_carro) > (salario * 0.30)):
    print("negado")
else:
    print("aprovado")





# Aprovador de Financiamento de Carros: Peça o valor do carro, o salário do comprador e a quantidade de
# meses para pagar. Se o valor da parcela mensal ultrapassar 30% do salário, o financiamento deve ser
# "Negado". Caso contrário, "Aprovado".