'''comissão por vendas'''
# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por
# cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve
# vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou
# seja, um total de $470. Escreva um programa (usando um array de contadores) que
# determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $+
tabela = [0, 0, 0]
const = 1
vendas = float(input('digite o total de vendas: '))
while vendas > 0:
    total = (vendas * 0.09) + 200
    if total >= 200 and total <= 299:
        tabela[0] += 1
    elif total >= 300 and total <= 399:
        tabela[1] += 1
    else:
        tabela[2] += 1
    vendas = float(input('digite o total de vendas: '))
for x in range(3):
    if x == 0:
        print(f'vendas de $200 - $299: {tabela[0]}')
    elif x == 1:
        print(f'vendas de $300 - $399: {tabela[1]}')
    elif x == 2:
        print(f'vendas de $400 - $+: {tabela[2]}')
