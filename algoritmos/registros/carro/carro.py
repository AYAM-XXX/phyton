'''criar um carro com 3 popriedades e 3 metodos'''


class Carro():
    def __init__(self, marca, motor, price):
        self.marca = marca
        self.tipo_do_motor = motor
        self.price_sell = price

    def search_price(self):
        print("pesquisando")

    def comprar(self):
        print("venda conlcuida")

    def informa(self):
        print(self.marca, self.tipo_do_motor, self.price_sell)


carroinf = Carro("nissan GTR", "V8", "80k")
carroinf.search_price()
carroinf.informa()
carroinf.comprar()
