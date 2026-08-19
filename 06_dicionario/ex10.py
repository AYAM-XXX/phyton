def menu():
    print("\n1- cadastro")
    print("2- exibir produtos")
    print("3- produto mais caro")
    print("4- valor total do estoque")
    print("5- quantidade de produtos cadastrados")
    print("6- fechar programa\n")

produtos = []
while True:
    menu()
    escolha = int(input("digite o numero: "))
    print("\n")
    match(escolha):
        case 1:
            produto = {}
            nome = input("digite o nome do produto: ")
            preco = float(input("digite o preco do produto: "))
            estoque = int(input("digite a quantidade no estoque: "))
            produto["nome"] = nome
            produto["preco"] = preco
            produto["estoque"] = estoque
            produtos.append(produto)
        case 2:
            for produto in produtos:
                print(f"nome: {produto["nome"]}\n"
                      f"preço: {produto["preco"]}\n"
                      f"estoque: {produto["estoque"]}\n")
        case 3:
            maior = float("-inf")
            for produto in produtos:
                if produto["preco"] > maior:
                    maior = produto["preco"]

            for produto in produtos:
                if produto["preco"] == maior:
                    print(f"nome: {produto["nome"]}\n"
                          f"preço: {produto["preco"]}\n"
                          f"estoque: {produto["estoque"]}\n")
        case 4:
            price = 0
            for produto in produtos:
                price += produto["preco"] * produto["estoque"]

            print(f"Quantidade total do estoque: {price:.2f}")

        case 5:
            print(f"Quantidade total de produtos: {len(produtos)}")
        case 6:
            print("fechando programa")
            break