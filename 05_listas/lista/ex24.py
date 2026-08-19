# 24. (Streaming): Crie uma lista com 5 músicas da sua playlist. Usando um laço while
# com decremento de variáveis, exiba as músicas na ordem inversa (do último índice até o
# índice 0).

playlist_musicas = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Imagine",
    "Stairway to Heaven",
    "Billie Jean"
]

for musica in reversed(playlist_musicas):
    print(musica)