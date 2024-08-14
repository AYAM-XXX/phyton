'''maior vendas do mes'''
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
vendas = [1200, 2000, 3000, 450, 1250, 2450, 3490, 1210, 3200, 1250.40, 2450, 423]
i = vendas.index(max(vendas))
j = vendas.index(min(vendas))
print(f'maior mes de vendas: {mes[i]}\n total de vendas: R${max(vendas)}')
print(f'menor mes de vendas: {mes[j]}\n total de vendas: R${min(vendas)}')
print(f'faturamento total: {sum(vendas)}')
print(f'porcentagem do maior valor em relação ao total: {(max(vendas) / sum(vendas)):.1%}')
top = []
top.append(max(vendas))
vendas.remove(max(vendas))
top.append(max(vendas))
vendas.remove(max(vendas))
top.append(max(vendas))
strin = [str(top) for top in top]
print(f'top 3 vendas: ')
print('\n'.join(strin))