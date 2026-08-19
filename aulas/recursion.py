lista = [0, 1, 2, 3, 4, 6]
x = 0
# maior = lista[0]
# for i in lista:
#     if i > maior:
#         maior = i
# print(maior)


def maioral(lista):
    if not lista:
        return 0
    return 1 + maioral(lista[1:])


print(maioral(lista))
print(len(lista))
