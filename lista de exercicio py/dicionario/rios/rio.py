# Rios: Crie um dicionário contendo os três principais rios e o país
# por onde cada rio passa.
# Um par chave-valor pode ser 'nile': 'egypt'.
# • Use um loop para exibir uma frase sobre cada rio, como:
# O Nilo atravessa o Egito.
# • Use um loop para exibir o nome de cada rio incluído no dicionário.
# • Use um loop para exibir o nome de cada país incluído no dicionário.
rios = {'nilo': 'egito', 'rio amazonas': 'brasil', 'rio Yangtzé': 'china'}
for rio, lugar in rios.items():
    print(f"O {rio.title()} atravessa o {lugar.title()}.")