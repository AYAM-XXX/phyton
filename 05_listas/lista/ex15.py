# 15.(Biblioteca): Crie uma lista de livros. Use um laço de repetição para percorrer a lista
# e contar quantos livros possuem o título exato de "Python Básico".

livros = [
    "O Senhor dos Anéis",
    "Dom Casmurro",
    "1984",
    "O Pequeno Príncipe",
    "Harry Potter",
    "Python Básico"
]

for livro in livros:
    if livro in "Python Básico":
        print("possui o livro Python Básico")