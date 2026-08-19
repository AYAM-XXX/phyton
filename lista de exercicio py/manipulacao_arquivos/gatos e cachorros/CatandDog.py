# Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene, pelo
# menos, três nomes de gatos no primeiro arquivo e três nomes de cachorros
# no segundo arquivo. Crie um programa que tente ler esses arquivos e exiba
# o conteúdo do arquivo na tela. Insira seu código em um bloco try-except
# para detectar o erro FileNotFound e exiba uma mensagem amigável se um
# arquivo estiver ausente. Transfira um dos arquivos para um local diferente
# em seu sistema e garanta que o código no bloco except seja devidamente
# executado.

from pathlib import Path
path = Path(
    'lista de exercicio py/manipulacao_arquivos/gatos e cachorros/gato.txt')
path2 = Path(
 'lista de exercicio py/manipulacao_arquivos/gatos e cachorros/cachorro.txt')
try:
    gatos = path.read_text()
    gatos = gatos.split()
    cachorros = path2.read_text()
    cachorros = cachorros.split()

except FileNotFoundError:
    print("arquivo não encontrado")
else:
    print("\nnome de gatos: ")
    for gato in gatos:
        print(gato)
    print("\nnome de cachorros: ")
    for cachorro in cachorros:
        print(cachorro)
