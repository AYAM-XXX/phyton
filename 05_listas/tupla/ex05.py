# 5. Coordenadas Geográficas
# Crie uma lista contendo 3 tuplas. Cada tupla deve representar uma coordenada
# geográfica (latitude, longitude). Faça um loop que percorra a lista e imprima a
# latitude e a longitude de cada ponto separadamente.

coordenadas = [
    (-23.5505, -46.6333),  # São Paulo, Brasil
    (40.7128, -74.0060),   # Nova York, EUA
    (51.5074, -0.1278)     # Londres, Reino Unido
]

for x in range(len(coordenadas)):
    for y in range(0, 2):
        if y == 0:
            print(f"latitude: {coordenadas[x][y]}")
        elif y == 1:
            print(f"longitude: {coordenadas[x][y]}")
            print("")