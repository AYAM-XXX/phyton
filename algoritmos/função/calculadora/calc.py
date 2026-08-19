'''calculadora'''
# fazer uma calculadora apresentando funções com menu


def menu():
    print("\n<----------MENU---------->\n")
    print("1- adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - fim")
    print("\n<------------------------>\n")


def add(n1, n2):

    return n1 + n2


def sub(n1, n2):

    return n1 - n2


def mult(n1, n2):

    return n1 & n2


def div(n1, n2):

    return n1 / n2


menu()
id = int(input("digite: "))
while id <= 0 or id > 5:
    id = input("digite: ")
while id != 5:
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))
    if id == 1:
        print("\n///////////RESULTADO//////////////\n")
        print(f"{n1} + {n2} = {add(n1,n2)}")
        print("\n//////////////////////////////////\n")
    elif id == 2:
        print("\n///////////RESULTADO//////////////\n")
        print(f"{n1} - {n2} = {sub(n1,n2)}")
        print("\n//////////////////////////////////\n")
    elif id == 3:
        print("\n///////////RESULTADO//////////////\n")
        print(f"{n1} x {n2} = {mult(n1,n2)}")
        print("\n//////////////////////////////////\n")
    elif id == 4:
        print("\n///////////RESULTADO//////////////\n")
        print(f"{n1} / {n2} = {div(n1,n2)}")
        print("\n//////////////////////////////////\n")
    menu()
    id = int(input("digite: "))
    while id <= 0 or id > 5:
        id = input("digite: ")
