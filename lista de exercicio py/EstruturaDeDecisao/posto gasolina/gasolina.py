'''calcular desconto'''
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o
# número de litros vendidos, o tipo de combustível
# (codificado da seguinte
# forma: A-álcool, G-gasolina), calcule e imprima o
# valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90
litros = int(input("quantos litros foram abastecidos: "))
tipo = input("g - gasolina\na - álcool\ndigite: ")

if tipo == 'a':
    if litros <= 20:
        print(f"valor total: R$ {(litros * 1.90) * 0.97}")
    else:
        print(f"valor total: R$ {(litros * 1.90) * 0.95}")
if tipo == 'g':
    if litros <= 20:
        print(f"valor total: R$ {(litros * 1.90) * 0.96}")
    else:
        print(f"valor total: R$ {(litros * 1.90) * 0.94}")
