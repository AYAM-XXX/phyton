from pathlib import Path

arquivos = ['lista de exercicio py/manipulacao_arquivos/contador/livro.txt',
            'lista de exercicio py/manipulacao_arquivos/contador/livro_02.txt']


def total_palavras(arquivo):
    try:
        ler = arquivo.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("não existe")
    else:
        ler = ler.split()
        palavra = input("digite a palavra que que encontrar: ")
        print(f"total do palavras: {len(ler)}")
        print(f"total de palavras '{palavra}': {ler.count(palavra)}")


for livro in arquivos:
    path = Path(livro)
    total_palavras(path)
