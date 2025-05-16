from pathlib import Path

livros = ['lista de exercicio py/manipulacao_arquivos/contador/livro.txt',
          'lista de exercicio py/manipulacao_arquivos/contador/livro_02.txt']


def contar_palavras(arquivo):
    try:
        path = Path(arquivo)
    except FileNotFoundError:
        print("arquivo não encontrado")
    ler = path.read_text(encoding='utf-8')
    palavras = ler.split()
    num_palavras = len(palavras)
    print(f"total de palavras: {num_palavras}")


for livro in livros:
    contar_palavras(livro)
