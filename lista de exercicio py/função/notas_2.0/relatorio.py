def exibir_notas(lista: dict[str: list[float]]):
    print("\n\n--------NOTA DOS ALUNOS--------\n")
    for nome, nota in lista.items():
        print("nome do aluno: ", nome.title())
        if nota:
            print("notas: ", nota)
            print(f"media: {sum(lista[nome]) / len(lista[nome]):.2f}")
        else:
            print("nota não cadastrada")
        print("\n\n")
