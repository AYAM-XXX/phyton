'''apredendo classes em python'''
# apredendo como criar e implementar classes


class Computador:
    def __init__(self, marca, memoria, placa):
        self.marca = marca
        self.memoria_ram = memoria
        self.placa_de_video = placa

    def ligar(self):
        print("ligando...")

    def desligar(self):
        print("desligando")

    def informa(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = Computador('Asus', '10gb', '2080')
computador1.ligar()
computador1.informa()
computador1.desligar()
