'''pedir lanche'''
# esse pograma ira simular o pedido de um lache em drive tru de um mcdonald


def cardapio():
    print("\n1 - big mac\n2- Brabo Melt Crispy\n3 - Duplo Quarterão")
    print("4- Cheddar McMelt\n5 - McFish")


def lanches(tp):
    if tp == 1:
        print('big mac')
    elif tp == 2:
        print('Brabo Melt Crispy')
    elif tp == 3:
        print('Duplo Quarterão')
    elif tp == 3:
        print('Cheddar McMelt')
    else:
        print('McFish')


def batata(tamanho):
    print(f"batata: {tamanho}")


def refri(tipo):
    print(f"refri {tipo}")


def pedido(nome, tp, tamanho, tipo):
    print(f"obrigado pela preferencia {nome}")
    lanches(tp)
    batata(tamanho)
    refri(tipo)


pedido('ayam', 2, 'grande', 'sprite')
