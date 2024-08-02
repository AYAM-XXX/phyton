''' verifica o numero'''
# Faça um Programa que leia 1 número e em seguida pergunte ao
# usuário qual
# operação ele deseja realizar. O resultado da operação deve ser
# acompanhado de
# uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.
n1 = float(input("digite o numero: "))
print("a. par ou ímpar;\nb. positivo ou negativo\nc. inteiro ou decimal")
escolha = input("digite a alternativa: ")
if escolha == 'a':
    if n1 % 2 == 0:
        print(f"{n1} e par")
    else:
        print(f"{n1} e impar")
elif escolha == 'b':
    if n1 > 0:
        print(f"{n1} e positivo")
    else:
        print(f"{n1} e negativo")
elif escolha == 'c':
    if n1.is_integer():
        print(f"{n1} e inteiro")
    else:
        print(f"{n1} e decimal")
