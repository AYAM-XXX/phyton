def calcular_media(nome, lista):
    if nome in lista:  # verifica se o nome está na lista
        nota = lista[nome]
        if nota:  # verifica se tem nota na lista
            media = (sum(nota) / len(lista[nome]))
            return media
        else:
            print("sem nota cadastrada")
            return None
    else:
        media = print("aluno não encontrado")
        return None
