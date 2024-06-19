'''nota de um aluno'''
# ler a nota de um determinado aluno e fazer p regsitro dela

dados = []


class aluno():
    def __init__(self):
        self.nome = ''
        self.n1 = ''
        self.n2 = ''
        self.n3 = ''

    def dado(self):
        for i in range(4):
            jk = []
            for x in range(4):
                if x == 0:
                    inf = input("digite o nome: ")
                else:
                    inf = float(
                        input(f"digite a nota do aluno do {x}° semestre: "))
                jk.append(inf)
            dados.append(jk)

    def exibir(self):
        ch = input("\ndeseja pesquisar?\nsim\nnão\ndigite:")
        while ch == 'sim':
            id = int(input("diga qual o numero do aluno: "))
            for x in range(4):
                if x == 0:
                    self.nome = dados[id][x]
                elif x == 1:
                    self.n1 = dados[id][x]
                elif x == 2:
                    self.n2 = dados[id][x]
                elif x == 3:
                    self.n3 = dados[id][x]
            print(f"nome do aluno: {self.nome}")
            print(f"\n1° semestre: {self.n1}")
            print(f"\n2° semestre: {self.n2}")
            print(f"\n3° semestre: {self.n3}")
            ch = input("\ndeseja continuar?\nsim\nnão\ndigite:")
            while ch != 'não' and ch != 'sim':
                ch = input("\ndeseja continuar?\nsim\nnão\ndigite:")


notas = aluno()
notas.dado()
notas.exibir()
