'''fazer implementações sobre vendas com tuplas'''
vendas = [
    ('20/08/2023', 'iphone 13', '256gb', 350, 10000),
    ('14/04/2022', 'iphone 12', '256gb', 250, 9000),
    ('10/06/2020', 'iphone 11', '256gb', 150, 8000),
    ('5/01/2019', 'iphone x', '256gb', 100, 7000),
    ('02/09/2018', 'iphone 8', '256gb', 130, 6000)
]
prtd_mais_vnd = ''
qtd_mais_vnd = 0
faturamento = 0
for item in vendas:
    data, tipo, tamanho, vendas, valor = item
    faturamento += vendas * valor
    if vendas > qtd_mais_vnd:
        qtd_mais_vnd = vendas
        prtd_mais_vnd = tipo
    if '20/08/2023' in data:
        print(f"faturamento de 2023: {vendas * valor:,}R$")
    if '14/04/2022' in data:
        print(f"faturamento de 2022: {vendas * valor:,}R$")
    if '10/06/2020' in data:
        print(f"faturamento de 2020: {vendas * valor:,}R$")
    if '5/01/2019' in data:
        print(f"faturamento de 2019: {vendas * valor:,}R$")
    if '02/09/2018' in data:
        print(f"faturamento de 2018: {vendas * valor:,}R$")

print(f'faturamento total: {faturamento:,}R$')
print(f'produto mais vendido: {prtd_mais_vnd}\nQuantidade: {qtd_mais_vnd:,}')
