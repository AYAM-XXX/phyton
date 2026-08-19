# Crie um programa que simule saques em um caixa eletrônico. O usuário
# digita o valor do saque (múltiplo de 10, entre 10 e 1000). O programa
# deve continuar pedindo valores até que o usuário digite 0. Para cada
# saque válido, calcule quantas notas de 100, 50, 20 e 10 são necessárias.
# Exiba o total de saques válidos e a quantidade total de cada tipo de
# nota ao final. Se o valor não for válido, exiba "Erro: Valor inválido!"
def saque(valor):
    notas100 = valor // 100
    resto = valor % 100
    print(f"valor de notas de 100: {notas100}")

    notas50 = resto // 50
    resto = resto % 50
    print(f"valor de notas de 50: {notas50}")

    notas20 = resto // 20
    resto = resto % 100
    print(f"valor de notas de 20: {notas20}")

    notas10 = resto // 10
    resto = resto % 100
    print(f"valor de notas de 10: {notas10}")


def validador(valor):
    if valor > 0 and valor % 10 == 0:
        return True
    else:
        return False


while True:
    valor = input("insira o valor do saque: ")
    try:
        valor = int(valor)
    except ValueError:
        print("valor incorreto")
    if valor != 0:
        if validador(valor):
            saque(valor)
        else:
            print("não aceitamos essa quantidade: ")
    else:
        break
