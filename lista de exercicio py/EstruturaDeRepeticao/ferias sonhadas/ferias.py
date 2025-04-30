# Férias tão sonhadas: Crie uma pesquisa que pergunte aos usuários
# sobre as férias de seus
# sonhos. Crie um prompt mais ou menos assim: Se pudesse visitar qualquer
# lugar do mundo,
# para onde iria? Inclua um bloco de código que exiba os resultados dessa
# pesquisa.

prompt = 'Se pudesse visitar qualquer lugar do mundo, para onde iria? '
lugares = {}
while True:
    nome = input('digite seu nome: ')
    if nome == 'sair':
        break
    else:
        lugar = input(prompt)
        lugares[nome] = lugar

for nome, lugar in lugares.items():
    print(f"O lugar favorito de {nome.title()} é {lugar.title()}")
