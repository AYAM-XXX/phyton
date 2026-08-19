# Pessoa: Use um dicionário para armazenar informações sobre uma
# pessoa que você conhece.
# Armazene o nome, sobrenome, idade e a cidade onde mora. Nomeie
# as chaves como first_name,
# last_name, age e city. Exiba cada informação armazenada em seu
# dicionário.
pessoas = []
isadora = {'first_name': 'isadora', 'idade': 17, 'cidade': 'uberlandia'}
ana = {'first_name': 'ana', 'idade': 19, 'cidade': 'uberlandia'}
giovanna = {'first_name': 'giovanna', 'idade': 21, 'cidade': 'uberlandia'}
pessoas.append(isadora)
pessoas.append(ana)
pessoas.append(giovanna)
for pessoa in pessoas:
    print(pessoa['first_name'])
    print(pessoa['idade'])
    print(pessoa['cidade'])
    print('\n')    