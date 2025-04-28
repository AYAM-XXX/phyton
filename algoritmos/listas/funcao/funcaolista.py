# Funções: Pense em coisas que você conseguiria armazenar em uma lista.
# Por exemplo, você pode criar uma lista de montanhas, rios, países,
# cidades, idiomas, ou qualquer outra coisa que quiser.
# Crie um programa com uma lista contendo esses itens e, em seguida,
# use cada função apresentada neste capítulo, pelo menos, uma vez.
coisas = ['carro', 'tenis', 'pinbolin', 'caçapa']
print(sorted(coisas))
print(len(coisas))
coisas.append('ratoeira')
coisas.append('chafariz')
coisas.append('fusca')
coisas.remove('carro')
coisas.pop(2)
del coisas[1]
coisas.sort()
coisas.reverse()
print(coisas)
