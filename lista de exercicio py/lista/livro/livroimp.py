'''atribuição de imposto para livro'''
# corrigir o valor do livro sobre impostos
items = ['computador', 'estante', 'ps5', 'livro', 'fonte']
qtd = [[200, 2500],
       [100, 350],
       [300, 3000],
       [450, 30],
       [100, 100]]
custo = 0
i = items.index('livro')
if 'livro' in items:
    qtd[i][1] = qtd[i][1] * 1.1
else:
    pass
print(f'impacto financiero de imposto: {(qtd[i][1] * qtd[i][0]) * 0.1}')
print(qtd)
