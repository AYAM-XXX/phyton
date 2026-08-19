produtos = []
for x in range(0,5):
    produto = {}
    produto["nome"] = input("insira o nome: ")
    produto["preço"] = float(input("insira o preço: "))
    produtos.append(produto)

for item in produtos:
    print(f"{item["nome"]}: {item["preço"]}")
