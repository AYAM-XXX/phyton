# Lugares favoritos: Crie um dicionário chamado favorite_places.
# Pense em três nomes para
# usar como chave no dicionário e armazene de um a três lugares
# favoritos para cada pessoa.
# Agora, para que este exercício fique ainda mais interessante,
# peça a alguns amigos que lhe
# digam alguns de seus lugares favoritos. Percorra o dicionário
# com um loop e exiba o nome de
# cada pessoa e seus lugares favoritos.

favorite_places = {
    'rio de janeiro': ['ana', 'giovanna', 'marcelo'],
    'silver spring': ['beatriz', 'yasmim', 'joão'],
    'caldas novas': ['luiza', 'elisa', 'carlos']
}

for place, name in favorite_places.items():
    print(f"city: {place}\nnames: {name}\n")