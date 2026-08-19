# 4.11 Minhas pizzas, suas pizzas: Comece com o programa do Exercício
# 4.1 (página 90). Faça
# uma cópia da lista de pizzas e a nomeie como friend_pizzas.
# Em seguida, siga as etapas:
# • Adicione uma pizza nova à lista original.
# • Adicione uma pizza diferente à lista friend_pizzas.
# • Prove que tem duas listas separadas. Exiba a mensagem:
# Minhas pizzas favoritas são:. E, em
# seguida, use um loop for para exibir a primeira lista.
# Exiba a mensagem: Minhas pizzas
# favoritas são:. E, em seguida, use um loop for para exibir
# a segunda lista. Garanta que cada
# pizza nova seja armazenada na lista adequada.

my_pizzas = ["Margherita", "Calabresa", "Quatro Queijos", "Frango com Catupiry", "Portuguesa", "Pepperoni"]
friend_pizzas = my_pizzas[:]
my_pizzas.append('cupim ao alho')
friend_pizzas.append('moda da casa')
print('minhas pizza favorita são: ')
for pizza in my_pizzas:
    print(pizza, end=", ")
print('\n pizza favorita do meu amigo são: ')
for pizza in friend_pizzas:
    print(pizza, end=", ")