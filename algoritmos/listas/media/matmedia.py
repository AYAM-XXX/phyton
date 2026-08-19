'''calcula a media de um numero de uma matriz'''
# calcula a media de um numero de uma matriz ja definida

notas = [[5.0, 4.5, 7.9, 8.9],
         [5.0, 6.7, 2.1, 4.0],
         [4.6, 3.8, 7.8, 6.7]]
soma = cont = 0
for x in range(len(notas)):
    for i in range(len(notas[x])):
        soma += notas[x][i]
        cont += 1
print(f"media das notas: {soma / cont}")
