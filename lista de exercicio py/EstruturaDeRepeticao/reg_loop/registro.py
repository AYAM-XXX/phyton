'''resgistrar produtos com while'''
produtos = []
produto = input("produto: ")
while produto != '':
    produtos.append(produto)
    produto = input("produto: ")
print(f'produtos registrados: {produtos}')