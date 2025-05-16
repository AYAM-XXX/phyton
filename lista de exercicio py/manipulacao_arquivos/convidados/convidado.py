# Livro de convidados: Escreva um loop while que solicite o nome dos usuários.
# Colete todos
# os nomes inseridos e, em seguida, escreva esses nomes em um arquivo chamado
# guest_book.txt.
# Garanta que cada item apareça em uma linha nova no arquivo.

from pathlib import Path

path = Path(
    'lista de exercicio py/manipulacao_arquivos/convidados/convidados.txt')
convidados = ''
while True:
    nome_convidado = input("digite o nome do convidado: ")
    if nome_convidado == "sair":
        path.write_text(convidados)
        break
    else:
        convidados += nome_convidado + '\n'

print(path.read_text())
