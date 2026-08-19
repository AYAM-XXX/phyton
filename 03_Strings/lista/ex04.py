# Nível Médio
#
# Exercício 4 (Contextualizado): Uma URL do sistema está estruturada assim:
#
# [loja.com/produtos/categoria/games/ps5](https://loja.com/produtos/categoria/games/ps5)".
# Crie um script que extraia apenas a palavra "games" e "ps5" dessa string utilizando fatiamento ou métodos de divisão

# link = "[loja.com/produtos/categoria/games/ps5](https://loja.com/produtos/categoria/games/ps5)"
# link = link.replace("/", " ").replace("]", " ").replace("[", " ").replace(".", " ").replace("(", " ").replace(")", " ").replace("//", " ").replace(":", " ")
# link = link.split()
# for character in link:
#     if (character in "ps5") or (character in "games"):
#         print(character)

# maneira certa de fazer o exercicio

link = "[loja.com/produtos/categoria/games/ps5](https://loja.com/produtos/categoria/games/ps5)"
print(link.find("games"))
print(link.find("ps5"))
print(link[29:34])
print(link[35:38])