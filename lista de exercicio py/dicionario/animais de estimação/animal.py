# Animais de estimação: Crie vários dicionários, em que cada dicionário
# representa um animal
# de estimação diferente. Em cada dicionário inclua o tipo de animal
# e o nome do dono. Armazene
# esses dicionários em uma lista chamada pets. Depois, percorra sua
# lista com um loop e, enquanto
# faz isso, exiba tudo o que sabe sobre cada animal de estimação.
pets = []

pet1 = {
    'tipo': 'cachorro',
    'nome_do_dono': 'ana'
}
pets.append(pet1)
pet2 = {
    'tipo': 'gato',
    'nome_do_dono': 'bruno'
}
pets.append(pet2)
pet3 = {
    'tipo': 'papagaio',
    'nome_do_dono': 'carla'
}
pets.append(pet3)
pet4 = {
    'tipo': 'hamster',
    'nome_do_dono': 'diego'
}
pets.append(pet4)
pet5 = {
    'tipo': 'peixe',
    'nome_do_dono': 'eduarda'
}
pets.append(pet5)

for pet in pets:
    print(f"type_of_animal: {pet['tipo']}\nowner: {pet['nome_do_dono'].title()}\n\n")