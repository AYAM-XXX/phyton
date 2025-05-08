def cadastrar(lista: dict[str: list[float]], nome: str) -> None:
    if nome not in lista:
        lista[nome] = {}
        print("\n\naluno cadastrado com sucesso :)\n\n")
    else:
        print("\naluno já cadastrado\n")
