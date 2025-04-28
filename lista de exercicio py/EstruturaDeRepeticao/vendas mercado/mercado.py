'''fazer um carrinho de vendas'''
# passar o produto e quantidade, quando terminar colocar como vazio
carrinho = []
produto = input("nome do produto: ")
qtd = int(input("digite a quantidade: "))
while True:
    carrinho.append([produto, qtd])
    produto = input("nome do produto: ")
    if not produto:
        break
    qtd = int(input("digite a quantidade: "))
print('produto comprados: ')
for x in range(len(carrinho)):
    print(f'{carrinho[x][0]}\nqtd: {carrinho[x][1]}x\n')