def cadastrar_aluno(lista, nome):
    if nome not in lista:  # vwrifica se o nome já está sendo usado
        lista[nome] = []  # add o nome e cria uma lista
    else:
        print("aluno já cadastrado")
