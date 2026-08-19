# Dada a lista de nomes de linguagens de programação ["Python",
# "JavaScript", "C#", "PHP"], utilize a estrutura de repetição com
# enumerate() para exibir as linguagens no formato de lista enumerada: "1 - Python", "2
# - JavaScript", etc.

lista = ["Python", "JavaScript", "C#", "PHP"]

for x,i in enumerate(lista):
    print(x,i)