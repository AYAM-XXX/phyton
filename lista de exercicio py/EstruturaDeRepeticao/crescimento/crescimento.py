'''comparar vendas'''
# comparar vendas com o ano passado
produtos = ['Iphone', 'Rog Phone', 'A30', 'ipad', 'Asus Phone']
ano_2023 = [2000, 2032, 3012, 1209, 9281]
ano_2024 = [4000, 5212, 2312, 209, 9281]

for i, item in enumerate(produtos):
    if ano_2024[i] > ano_2023[i]:
        print(f"produto: {item}\ncrescimento: {ano_2024[i] / ano_2023[i] - 1:.0%}")
    elif ano_2024[i] < ano_2023[i]:
        print(f"produto: {item}\ndecrescimento: {(ano_2024[i] / ano_2023[i] - 1)  * -1:.0%}")
    else:
        print(f"produto: {item}\nmesmo patamar do ano anterior")