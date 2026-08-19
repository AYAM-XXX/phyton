# Cidades: Crie um dicionário chamado cities. Utilize o nome
# de três cidades como chaves de
# seu dicionário. Crie um dicionário de informações sobre cada
# cidade e inclua o país em que a
# cidade está, sua população aproximada e um fato sobre essa
# cidade. O nome das chaves para o
# dicionário de cada cidade devem ser alguma coisa como country,
# population e fact. Exiba o
# nome de cada cidade e todas as informações que você armazenou a respeito.

cities = {
    'paris': {
        'país': 'França',
        'população': '2.1 milhões',
        'fato': 'É conhecida como a Cidade Luz.'
    },
    'nova_iorque': {
        'país': 'Estados Unidos',
        'população': '8.5 milhões',
        'fato': 'É onde fica a Estátua da Liberdade.'
    },
    'tóquio': {
        'país': 'Japão',
        'população': '13.9 milhões',
        'fato': 'É a maior cidade do mundo em população.'
    }
}

for city, facts in cities.items():
    country = facts['país'].title()
    population = facts['população']
    fato = facts['fato']

    print(f"city: {city.title()}")
    print(f"country: {country}")
    print(f"population: {population}")
    print(f"facts: {fato}\n")
