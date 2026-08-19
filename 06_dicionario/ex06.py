produtos = []

for x in range(0, 5):
    produto = {}
    nome = input("digite o nome do produto: ")
    produto["nome"] = nome
    produtos.append(produto)

for produto in produtos:
    print(f"{produto.get("nome")}")