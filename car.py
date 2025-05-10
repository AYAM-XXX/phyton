class car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ler_kilometragem = 200

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


meu_nissan = car(marca='toyota', ano='2024', modelo='r35 gtr')

print(meu_nissan.info())
meu_nissan.definir_km(100)
meu_nissan.kilometragem()
