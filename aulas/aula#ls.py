'''trabalhando com lista'''
produtos = ['mouse', 'headset', 'teclado', 'monitor']
produtos_2 = ['mousepad', 'gabinete', 'cadeira']
qtd = [100, 200, 30, 50, 800, 611, 23]
produtos.extend(produtos_2)
menos = min(produtos)
maior = max(produtos)
# produtos.sort(reverse=True) ordena e inverte tudo
produto = input("digite o produto que está procurando: ")
if produto in produtos:
    i = produtos.index(produto)  # .idex indica aonde está o item desejado
    print(f"produto: {produtos[i]}\n indice: {i}")
    print(f"produto mais vendido foi {maior}\n")
    print(f"produto menos vendido foi {menos}\n")
    print("items disponiveis:")
    print('\n'.join(produtos))  # escreve os items separados por um character
else:
    print("produto não encontrado")
# remove item
remv = input("digite o item que quer remover: ")
try:
    produtos.remove(remv)  # remove = exclui por nome  pop = exclui por item
    print('\n'.join(produtos))
    print(len(produtos))
except:
    print("produto não encontrado")
