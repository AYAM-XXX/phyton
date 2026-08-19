'''analisar o estoque da fabrica'''
# analisar o estoque de cada fabrica

estoque = [
    [200, 499, 100, 10, 10],
    [400, 40, 212, 234, 100],
    [200, 204, 145, 123, 45]
    ]
fabricas = ['arroz company', 'bovino algazes', 'algatimo factory']
minimox = 50
abaixo_estoque = []
for i, lista in enumerate(estoque):
    for lista2 in lista:
        if lista2 < minimox:
            if fabricas[i] in abaixo_estoque:
                pass
            else:
                abaixo_estoque.append(fabricas[i])
print('fabrica que tem produtos a baixo do estoque: \n')
for item in abaixo_estoque:
    print(item)