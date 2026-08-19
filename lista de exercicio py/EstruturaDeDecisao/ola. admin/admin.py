# Olá, admin: Crie uma lista com cinco ou mais nomes de usuários,
#  incluindo o nome 'admin'.
# Imagine que está escrevendo um código que exibirá uma mensagem 
# de boas-vindas aos
# usuários, após cada um deles logar em um site. Percorra a lista 
# com um loop e exiba uma
# mensagem de boas-vindas para cada usuário.
# • Se o nome de usuário for 'admin', exiba uma mensagem especial, 
# tipo: Olá administrador,
# gostaria de ver um relatório de status?
# • Caso contrário, exiba uma mensagem genérica, como: Olá Jaden, 
# obrigado por fazer login
# novamente.

usuarios = [
    "admin",
    "joao_silva",
    "maria123",
    "pedro.alves",
    "carla_oliveira"
]
novos_usuarios = [
    "lucas_ferreira",
    "ana.paula",
    "ricardo_melo",
    "beatriz.souza",
    "carla_oliveira"
]
if novos_usuarios:
    for usuario in novos_usuarios:
        if usuario.lower() in usuarios:
            print(f"Olá {usuario}, ja esta em uso")
        else:
            print('novo usuario add com sucesso')
else:
    print('lista vazia')

for usuario in usuarios:
    if usuario == 'admin':
        print("bom dia administrador")
    else: 
        print(f"Olá {usuario}, obrigado por fazer login")
