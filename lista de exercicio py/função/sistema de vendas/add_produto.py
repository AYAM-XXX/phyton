import validar_inputs_num as valid


def adicionar_produto(produtos: dict[str, int, float]) -> None:
    nome_produto = input("insira o nome do produto: ").lower()

    # verifica se ja tem um produto cadastrado
    if nome_produto not in produtos:
        produtos[nome_produto] = {}

        # pega a qtd de produtos e faz validação
        qtd_produto = valid.validador_num('insira a quantidade: ', int)
        produtos[nome_produto]['quantidade'] = qtd_produto

        # pega o valor do produto e faz validação
        preco_produto = valid.validador_num('insira o preço: ', float)
        produtos[nome_produto]['preço'] = preco_produto
    else:
        print("produto já existente")  # caso o produto ja existir
