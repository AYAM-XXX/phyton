# Números favoritos: Use um dicionário para armazenar os números
# favoritos das pessoas.
# Pense em cinco nomes e os utilize como chaves em seu dicionário.
# Pense em um número
# favorito para cada pessoa e armazene cada um como um valor em seu dicionário.
# Exiba o nome
# de cada pessoa e seu número favorito. Para que tudo fique ainda mais
#  divertido, pergunte a
# alguns amigos e obtenha alguns dados reais para o seu programa.

numeros_favorito = {
    "Ana": [1, 3, 4, 5],
    "Bruno": [6, 2, 4, 5],
    "Carla": [2, 3, 0, 5],
    "Diego": [3, 9, 2, 5],
    "Eduarda": [3, 4, 7, 5]
}

for nome, num in numeros_favorito.items():
    print(f"{nome}: {num}\n")
