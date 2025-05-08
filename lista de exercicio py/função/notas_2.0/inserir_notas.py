import loop_inserir as loop


def inserir_nota(lista: dict[str: list[float]],
                 nome: str, nota_nao_inserida) -> None:
    if nome in lista:
        nota_inserida = loop.inserir(nota_nao_inserida)
        lista[nome] = nota_inserida
    else:
        print("\naluno não cadastrado\n")
