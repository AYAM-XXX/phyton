def inserir_nota(nome, notas, lista):
    if nome in lista:  # verifica se o nome existe na lista
        lista[nome].extend(notas)  # adiciona as nota ao nome
        print("nota inserida com sucesso :)")
    else:
        print("aluno não encontrado")
