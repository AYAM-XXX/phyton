import add_produto as add
import validar_inputs_num as valid
import vender_produto as sell
import mostra_estoque as m_e
estoque = {}


def menu():
    print("\n+----MENU----+")
    print("1- add produto")
    print("2- vender produto")
    print("3- ver estoque")
    print("4- sair")


while True:
    menu()
    # não fiz casting pq n iria trabalhar com esse numero em operação mat
    escolha = input("digite o numero: ")
    match escolha:
        case "1":
            add.adicionar_produto(estoque)
        case "2":
            nome = input("insira o nome do produto: ").lower()
            quantidade = valid.validador_num(
                'qual a quantidade solicitada: ', int)
            sell.vender(nome=nome, qtd=quantidade, produtos=estoque)
        case "3":
            m_e.exibir(estoque)
        case "4":
            break
        case _:
            print("digite novamente :/")
