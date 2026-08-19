'''achar o indice do produto'''
# busca o indice de um certo produto para fazer buscas
produto = ['mouse', 'teclado', 'cpu', 'monitor', 'placa de video']
qtd = ['100', '200', '50', '350', '90']
name = input("digite o nome do produto que deseja procurar: ")
if name in produto:
    i = produto.index(name)
    print(f"produto: {produto[i]}\nquantidade: {qtd[i]}")
else:
    print("produto não encontrado")
