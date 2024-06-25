'''função soma'''
# definir uma função que retorna 2 numeros da soma


def soma(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def potencia(n1, n2):
    return n1 ** n2


def menu():
    print("\n<----------MENU---------->\n")
    print("1- adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - potencia")
    print("6- fim")
    print("\n<------------------------>\n")


menu()
id = int(input("digite sua escolha: "))
while id < 1 or id > 6:
    id = int(input("digite sua escolha: "))
while id != 6:
    num_1 = int(input("digite o primeiro numero: "))
    num_2 = int(input("digite o segundo numero: "))
    if id == 1:
        print(f"\nresultado: {soma(num_1, num_2)}")
    elif id == 2:
        print(f"\nresultado: {sub(num_1, num_2)}")
    elif id == 3:
        print(f"\nresultado: {mult(num_1, num_2)}")
    elif id == 4:
        print(f"\nresultado: {div(num_1, num_2)}")
    else:
        print(f"\nresultado: {potencia(num_1, num_2)}")
    menu()
    id = int(input("digite sua escolha: "))
    while id < 1 or id > 6:
        id = int(input("digite sua escolha: "))
