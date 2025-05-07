def exibir(produtos: dict[str, int]) -> None:
    print("\n+-----------produtos em estoque-----------+")
    # busca dicionario dentro de um dicionario
    for produto, info in produtos.items():
        print(f"nome do produto: {produto}")
        for key, value in info.items():  # imprime esse dicionario
            print(f"{key}: {value}")
        print("\n")
