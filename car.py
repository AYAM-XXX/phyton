class car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ler_kilometragem = 0

    def kilometragem(self):
        print(f"- kilometragem: {self.ler_kilometragem}")

    def info(self):
        infomacao = (
            f"- marca: {self.marca}\n- modelo: {self.modelo}\n- ano: {self.ano}")

        return infomacao

    def definir_km(self, km: int):
        if km > self.ler_kilometragem:
            self.ler_kilometragem = km
        else:
            print("isso n faz sentido")

    def fill_gas_tank(self):
        print(" 60l max")


class bateria():
    def __init__(self, tamanho_bateria=40):
        self.tamanho_bateria = tamanho_bateria

    def batery_size(self, tam):
        if tam >= self.tamanho_bateria:
            self.tamanho_bateria = tam
        else:
            print("numero incorrerto")

    def ler_bat(self):
        print(f"- tamanho da bateria: {self.tamanho_bateria}-kWh")


class ElectricCar(car):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.batery = bateria()

    def fill_gas_tank(self):
        print("- não tem tanque de combustivel")


meu_nissan = car(marca='toyota', ano='2024', modelo='r35 gtr')
meu_tesla = ElectricCar(marca='tesla', modelo='cybertruck', ano='2024')

print(meu_nissan.info())
meu_nissan.definir_km(100)
meu_nissan.kilometragem()
meu_nissan.fill_gas_tank()
print("\n", meu_tesla.info())
meu_tesla.batery.batery_size(100)
meu_tesla.batery.ler_bat()
meu_tesla.fill_gas_tank()
