'''lista telefonica'''
# fazer uma lista telefonica que contém endereços telefones, nomes
dados = []
ps = 3


class lista():
    def __init__(self):
        self.nome = ''
        self.tel = ''
        self.end = ''

    def cad(self):
        for x in range(ps):
            ent = []
            for i in range(3):
                if i == 0:
                    inf = input("digite o nome: ")
                    inf.lower()
                elif i == 1:
                    inf = input("digite o endereço: ")
                    inf.lower()
                elif i == 2:
                    inf = int(input("digite o telefone: "))
                    while inf < 0:
                        inf = int(input("digite o telefone: "))
                ent.append(inf)
            dados.append(ent)

    def search(self):
        ch = input("deseja pesquisar?\n-sim\n-não\ndigite: ")
        while ch != 'sim' and ch != 'não':
            ch = input("deseja pesquisar?\n-sim\n-não\ndigite: ")
        while ch == 'sim':
            id = int(input('digite o codigo de consulta: '))
            while id < 0 or id >= ps:
                id = int(input('digite o codigo de consulta existente: '))
            self.nome = dados[id][0]
            self.end = dados[id][1]
            self.tel = dados[id][2]
            print("\n---------------------------------------------")
            print(
                f"nome: {self.nome}  endereço: {self.end} telefone: {self.tel}")
            print("---------------------------------------------\n")
            ch = input("deseja pesquisar?\n-sim\n-não\ndigite: ")
            while ch != 'sim' and ch != 'não':
                ch = input("deseja pesquisar?\n-sim\n-não\ndigite: ")

    def ordena(self):
        for x in range(ps):
            for i in range(3):
                if dados[x][0] < dados[i][0]:
                    dados[x][0], dados[i][0] = dados[i][0], dados[x][0]
        for x in range(ps):
            print("\n---------------------------------------------")
            print(print(
                f"nome: {dados[x][0]}  endereço: {dados[x][1]} telefone: {dados[x][2]}"))
            print("---------------------------------------------\n")


listatel = lista()
listatel.cad()
listatel.search()
listatel.ordena()
