# 3.Escreva um script que solicite o nome completo de um usuário. O loop de validação
# não deve aceitar nomes vazios (com zero caracteres) ou strings compostas apenas por
# espaços em branco.

name = input("Enter name: ")
while name == "" or name.isspace():
    name = input("Enter name correct: ")

print(name)

