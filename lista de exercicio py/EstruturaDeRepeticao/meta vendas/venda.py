'''porcentagem de pessoas que bateram a venda'''
# calcular o quanto de pessoas bateram a venda

vendas = [
    ['antonio', 2000],
    ['karl', 50],
    ['ana', 450],
    ['mario', 3000],
    ['antonio', 50],
    ['marto', 1000]
]
meta = 500
soma = 0
colab_meta = []
for i, colab in enumerate(vendas):
    if vendas[i][1] >= meta:
        colab_meta.append(vendas[i][0])
print(f'porcentagem de pessoas que bateram a meta: {(len(colab_meta)/len(vendas)):.0%}')
print('vendedores que bateram a meta:') 
print('\n'.join(colab_meta))
