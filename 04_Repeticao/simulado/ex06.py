# Questão 6 – Sistema de Atendimento de
# uma Lanchonete (1,0 ponto)
# Uma lanchonete está substituindo sua calculadora por um pequeno sistema para realizar
# operações matemáticas durante o fechamento do caixa.
# Enquanto o operador estiver utilizando o sistema, deverá ser apresentado o seguinte
# menu:
# • 1 – Somar
# • 2 – Subtrair
# • 3 – Multiplicar
# • 4 – Dividir
# • 5 – Encerrar
# Sempre que uma operação for escolhida, o sistema deverá solicitar dois números,
# realizar o cálculo correspondente e apresentar o resultado.
# Caso o usuário informe uma opção inexistente, uma mensagem de erro deverá ser
# apresentada e o menu deverá ser exibido novamente.

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

