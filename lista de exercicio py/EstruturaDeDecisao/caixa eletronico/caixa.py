'''caixa eletronico'''
# . Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais
# é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
# quantidade de notas existentes na máquina.
# a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
# de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de
saque = int(input("digite a quantidade do saque: "))
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0
if saque < 10 or saque > 600:
    print("valor invalido")
else:
    if saque >= 100:
        notas100 = saque // 100
        saque = saque % 100

    if saque >= 50:
        notas50 = saque // 50
        saque = saque % 50

    if saque >= 10:
        notas10 = saque // 10
        saque = saque % 10

    if saque >= 5:
        notas5 = saque // 5
        saque = saque % 5

    if saque >= 1:
        notas1 = saque

    if notas100 > 0:
        print(f"notas de 100: {notas100}")
    if notas50 > 0:
        print(f"notas de 50: {notas50}")
    if notas10 > 0:
        print(f"notas de 10: {notas10}")
    if notas5 > 0:
        print(f"notas de 5: {notas1}")
    if notas1 > 0:
        print(f"notas de 1: {notas1}")
