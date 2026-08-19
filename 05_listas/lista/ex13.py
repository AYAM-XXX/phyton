# 13. (Controle de Acesso): Crie uma lista com 5 nomes de usuários cadastrados no
# banco de dados. Peça para o usuário digitar seu login e, utilizando o operador de
# pertinência (sem usar laços), exiba se ele possui acesso permitido ou se não foi
# encontrado.

nomes = ["Kaio", "Jones", "Mario", "heitor", "Bruno"]

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")

if nome.capitalize() in nomes:
    print("Acesso permitido")
else:
    print("Acesso negado")