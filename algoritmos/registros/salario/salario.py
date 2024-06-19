'''informa o salario e o cargo de acordo com a profissão'''
# fazer um pograma de pesquisa quantas vezes quiser o cargo é salario pelo codigo

dados = []
ok = 5


class cargo():
    def __init__(self):
        self.cargo = ''
        self.salario = ''

    def recolhe(self):

        for x in range(ok):
            dt = []
            for i in range(2):
                if i == 0:
                    dd = input("digite o cargo: ")
                else:
                    dd = float(input("digite o salario: "))
                    while dd <= 0:
                        dd = float(input("digite o salario: "))
                dt.append(dd)
            dados.append(dt)

    def exibir(self):
        print("\n-----------------------------------\n")
        for x in range(ok):
            print(
                f"\ncodigo: [{x}]   cargo: {dados[x][0]}   salario: {dados[x][1]}")
        print("\n-----------------------------------\n")

    def search(self):

        ch = input("deseja pesquisar?\n- sim\n- não\ndigite: ")
        while ch != 'sim' and ch != 'não':
            ch = input("deseja pesquisar?\n- sim\n- não\ndigite: ")
        while ch == 'sim':
            id = int(input("digite o codigo: "))
            self.cargo = dados[id][0]
            self.salario = dados[id][1]
            print("\n-----------------------------------")
            print(
                f"codigo: [{id}]   cargo: {self.cargo}   salario: {self.salario}")
            print("-----------------------------------\n")
            ch = input("deseja pesquisar denovo?\n- sim\n- não\ndigite: ")
            while ch != 'sim' and ch != 'não':
                ch = input("deseja pesquisar denovo?\n- sim\n- não\ndigite: ")


profissao = cargo()
profissao.recolhe()
profissao.search()
profissao.exibir()
