# Restaurante: Crie uma classe chamada Restaurant. O método __init__() para
# Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.
# Crie um método chamado describe_restaurant() que exiba essas duas informações
# e um método chamado open_restaurant() que exiba uma mensagem sinalizando que
# o restaurante está aberto.
# Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois
# atributos individualmente e, em seguida, chame ambos os métodos.

# Três restaurantes: Comece com sua classe do Exercício 9.1. Crie três
# instâncias diferentes da classe e chame describe_restaurant() para
# cada instância.

# Pessoas atendidas: Comece com o seu programa do Exercício 9.1 (página 208).
# Adicione um atributo chamado number_served com um valor default de 0.
# Crie uma instância chamada restaurant a partir dessa classe. Exiba o
# número de clientes que o restaurante atendeu e, em seguida, altere este
# valor e o exiba novamente.
# Adicione um método chamado set_number_served() que possibilita definir o
# número de clientes atendidos. Chame esse método com um novo número e
# exiba mais uma vez o valor.
# Adicione um método chamado increment_number_served(), o qual possibilita
# aumentar o número de clientes atendidos. Chame esse método com qualquer
# número que quiser e que possa representar quantos clientes foram atendidos
# em, digamos, um dia de atividade comercial.

class restaurante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"nome do restaurante: {self.restaurant_name.title()}")
        print(f"tipo de cozinha: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} está aberto")

    def set_number_served(self, num=0):
        if num >= self.number_served:
            self.number_served = num
        else:
            print('valor incompativel')

    def increment_number_served(self, add):
        if add > 0:
            self.number_served += add
        else:
            print('valor incompativel')


indian_food = restaurante('salamaleco_guys', 'indian')

indian_food.describe_restaurant()
indian_food.open_restaurant()

pastelaria = restaurante('pastelaria_du_tuax', 'pastelaria')
pastelaria.describe_restaurant()
pastelaria.open_restaurant()

pizza = restaurante("pizzapac", 'pizza')
pizza.describe_restaurant()
pizza.open_restaurant()
pizza.set_number_served(100)
print(f"numero de pessoas atendidas: {pizza.number_served}")
pizza.increment_number_served(100)
print(f"numero de pessoas atendidas: {pizza.number_served}")
