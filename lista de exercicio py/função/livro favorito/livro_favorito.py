# Livro favorito: Escreva uma função chamada favorite_book()
# que aceite um parâmetro, title.
# A função deve exibir uma mensagem como: Um dos meus livros
# favoritos é Alice no País das
# Maravilhas. Chame a função e lembre-se de incluir o título
# de um livro como argumento na
# chamada da função.

def favorite_book(title, author='desconhecido', ano=''):
    title = f"livro: {title.title()}"
    author = f"\nAutor: {author.title()}"
    if ano:
        ano = f"\nAno: {ano}"
    return title + author + ano


livro = favorite_book(title='capitães da areia', author='jorge amado')
print(livro)
