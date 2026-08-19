# 10. Desenvolva um menu que permita ao usuário:
# o Somar dois números;
# o Subtrair dois números;
# o Multiplicar dois números;
# o Dividir dois números;
# o Encerrar o programa.
# O menu deve continuar sendo exibido até o usuário escolher sair

def menu():
    print("1 – Somar \n 2 – Subtrair \n 3 – Multiplicar\n 4 – Dividir\n 5 – Encerrar")

isValid = True

while isValid:
    menu()
    choice = int(input("Enter a number: "))
    match choice:
        case 1:
            num1 = int(input("Enter a number:"))
            num2 = int(input("Enter a number:"))
            print(f"result of the sum: {num1 + num2}")
        case 2:
            num1 = int(input("Enter a number:"))
            num2 = int(input("Enter a number:"))
            print(f"result of the subtraction: {num1 - num2}")
        case 3:
            num1 = int(input("Enter a number:"))
            num2 = int(input("Enter a number:"))
            print(f"result of the multiplication: {num1 * num2}")
        case 4:
            num1 = int(input("Enter a number:"))
            num2 = int(input("Enter a number:"))
            if num2 == 0:
                print("It's impossible division by zero")
            else:
                print(f"result of the division: {num1 + num2}")

        case 5:
                isValid = False
        case _:
            print("incorrect syntaxe, enter another number")