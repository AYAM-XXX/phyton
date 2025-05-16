from pathlib import Path


nome_arquivo = input("digite o nome da prova: ").strip() + '.txt'
pasta = Path('lista de exercicio py/manipulacao_arquivos/gabarito/provas')
pasta.mkdir(parents=True, exist_ok=True)
arquivo = pasta / nome_arquivo
arquivo.touch(exist_ok=True)


def preencher():
    resposta = ''
    valores_validos = {'a', 'b', 'c', 'd'}
    for i in range(1, 31):
        print(f"questão {i}")
        while True:
            gabarito = input("digite a opcão: ")
            if gabarito in valores_validos:
                break
            print("\nescreva corretamente\n")
        resposta += f"{i}- {gabarito}\n"
        print("\n")
    arquivo.write_text(resposta)


preencher()
print(arquivo.read_text())
