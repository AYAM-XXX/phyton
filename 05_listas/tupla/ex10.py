# 10. Divisão de Tipos
# Dada uma tupla misturada: itens = (10, "Python", 20, "Programação", 30, "Tuplas").
# Crie duas listas vazias. Percorra a tupla e, usando a função type(), coloque os
# números inteiros em uma lista e as strings na outra. No final, converta as duas
# listas de volta para tuplas e exiba-as

itens = (10, "Python", 20, "Programação", 30, "Tuplas")

inteiros = []
palavras = []
for item in itens:
    if(type(item) == int):
        inteiros.append(item)
    else:
        palavras.append(item)
inteiros = tuple(inteiros)
palavras = tuple(palavras)
print(palavras)
print(inteiros)