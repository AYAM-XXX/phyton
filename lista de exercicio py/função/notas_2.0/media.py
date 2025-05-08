def media_nota(lista: dict[str: list[float]], nome: str):
    if nome in lista:
        if lista[nome]:
            media = sum(lista[nome]) / len(lista[nome])
            print(f"\n\naluno: {lista[nome]}")
            print(f"media do aluno: {media:.2f}\n\n")
        else:
            print("\nalunos sem nota cadastrada\n")
    else:
        print("\nnome não encontrado\n")
