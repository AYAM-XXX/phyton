def vender(nome: str, qtd: int,
           produtos: dict[str, int | float | str]) -> None:

    if nome in produtos:
        # verifica se tem quantidade suficiente no estoque
        if produtos[nome]['quantidade'] > qtd:
            produtos[nome]['quantidade'] -= qtd  # diminui qtd do estoque
            print("\nvenda realizada com sucesso :)")
            print(f"quantidade vendida: {qtd}")
            print(f"valor total: {produtos[nome]['preço'] * qtd} R$")
        else:
            # caso o estoque for menor que a qtd solicitada
            print("não temos estoque suficiente")
    else:
        print('produto não encontrado')  # nome do produto invalido
