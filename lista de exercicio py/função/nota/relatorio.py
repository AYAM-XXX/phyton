def relatorio(lista):
    if lista:  # verifica se a lsita não está vazia
        print("\n=====relatorio de alunos=====\n")
        for key, value in lista.items():  # imprime o relatorio
            print(f"Aluno: {key.title()}")
            if value:  # verifica se tem notas
                print(f"nota: : {value}")
                media = sum(lista[key]) / len(lista[key])
                print(f"media: {media}\n")
            else:
                print("nota não cadastrada")
    else:
        print("\nnenhum aluno cadastrado\n")
