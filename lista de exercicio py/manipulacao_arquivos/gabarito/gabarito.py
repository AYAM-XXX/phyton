from pathlib import Path


nome_arquivo = input("digite o nome da prova: ") + '.txt'
pasta = Path('lista de exercicio py/manipulacao_arquivos/gabarito/provas')
arquivo = pasta / nome_arquivo
arquivo.touch()


def preencher():
    resposta = ''
    for i in range(1, 31):
        print(f"questão {i}")
        gabarito = input("digite a opcão: ")
        resposta += f"{i}- {gabarito}\n"
        print("\n")
    arquivo.write_text(resposta)


preencher()
print(arquivo.read_text())
