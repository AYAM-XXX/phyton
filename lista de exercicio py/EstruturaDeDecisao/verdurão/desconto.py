'''desconto respectivo'''
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total
# da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10%
# sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de
# morangos e a
# quantidade (em Kg) de maças adquiridas e escreva o valor
# a ser pago pelo cliente
kg = int(input("quantidade de kg: "))
print("mo - morango\nma - maça\n")
esc = input("digite: ")
if esc == "mo":
    if kg <= 5:
        print(f"preço: R$ {kg * 2.50:.2f}")
    elif kg >= 25:
        print(f"preço: R$ {(kg * 2.20) * 0.90:.2f}")
    else:
        print(f"preço: R$ {kg * 2.20:.2f}")
elif esc == "ma":
    if kg <= 5:
        print(f"preço: R$ {kg * 1.80:.2f}")
    elif kg >= 25:
        print(f"preço: R$ {(kg * 1.50) * 0.90:.2f}")
    else:
        print(f"preço: R$ {kg * 1.50:.2f}")
else:
    print("erro")
