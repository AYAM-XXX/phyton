class veiculo():
    def __init__ (self, rodas, portas, combustivel, motor):
        self.rodas = rodas
        self.portas = portas
        self.combustivel = combustivel
        self.motor = motor


carro = veiculo(4, 4, "gasolina", "combustão")



class estudante():
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return  (self.nota1 + self.nota2) / 2

    def mudar_nome(self, nome):
        self.nome = nome

        print(f"nome definido: {self.nome}")


ana = estudante("Ana", 16, 7, 7)

# valores = vars(ana)
# print(valores)

print(ana.calcular_media())
ana.mudar_nome("Ana Carolina")