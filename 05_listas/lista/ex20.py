# (Mídias Sociais): Crie uma lista com as postagens de um usuário. Remova o último
# post publicado utilizando o método de exclusão por posição que limpa o fim da lista
# automaticamente

todas_as_postagens = [
    {"usuario": "maria", "texto": "Adorei o dia!"},
    {"usuario": "joao123", "texto": "Estudando Python hoje."},
    {"usuario": "joao123", "texto": "Mais um post sobre programação."}
]

for postagem in todas_as_postagens:
    print(postagem)
todas_as_postagens.pop()
print("\n\n\n\n\n\n\n")

for postagem in todas_as_postagens:
    print(postagem)
