# Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com o nome de
# diversos
# sanduíches. Depois, crie uma lista vazia chamada finished_sandwiches.
# Percorra a lista de
# pedidos de sanduíches com um loop e exiba uma mensagem para cada pedido,
#  como: Seu lanche
# de atum está pronto. Conforme cada sanduíche é preparado, passe-os para a
#  lista de sanduíches
# prontos. Após todos os sanduíches terem sido preparados, exiba uma mensagem
# enumerando
# cada um deles.

sandwich_orders = ['xtudo', 'xbacon', 'xsalada', 'xpicanha',
                   'xlombo', 'xlombo', 'xlombo', 'xlombo', 'xlombo']
finished_sandwiches = []
# inverto á lista para utilizar ela na ordem correta ao aplicar o .pop()
sandwich_orders.reverse()
print("não temos lombo hoje :(")
while 'xlombo' in sandwich_orders:
    sandwich_orders.remove('xlombo')
    print('removendo item...')

print('\n')
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
    print(f"{order} está pronto!!!")

print("\n\nlista de pedidos\n")
for num in range(len(finished_sandwiches)):
    print(f"{num + 1} - {finished_sandwiches[num].title()}")
