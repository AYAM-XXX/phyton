# Uma biblioteca digital identificou que muitos usuários cadastravam títulos de livros
# utilizando diferentes padrões de escrita, dificultando as pesquisas realizadas no sistema.
# Para minimizar esse problema, foi solicitado o desenvolvimento de um programa capaz
# de fornecer algumas informações sobre cada título informado.
# O programa deverá:
# • solicitar o título de um livro;
# • informar a quantidade de caracteres;
# • apresentar o título em letras maiúsculas;
# • apresentar o título em letras minúsculas.
# Após cada cadastro, o sistema deverá perguntar se o usuário deseja cadastrar outro livro,
# permanecendo em execução até que seja escolhida a opção de encerramento.


while True:
    name = input("Enter book name:")
    print(f"Total character: {len(name)}")
    print(f"{name.upper()}")
    print(f"{name.lower()}")
    choice = int(input("User wish register another book? 1- yes/2- no: "))
    if choice == 1:
        continue
    else:
        break
