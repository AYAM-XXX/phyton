# 1.Crie um script que peça a digitação de um número positivo e exiba o seu quadrado. O
# loop deve perguntar ao final se o usuário deseja efetuar o cálculo para outro número.
# Garanta que o cálculo seja feito pelo menos uma vez antes da pergunta.


while True:
    num = int(input("Enter a number: "))
    while num < 0:
        num = int(input("Enter a number: "))
    quadratic = num **2
    print(f"Square of this number: {quadratic}")
    answer = int(input("Do u want to do a new calculation? 1- yes/2- no:"))
    if(answer == 2):
        break
    else:
        continue

