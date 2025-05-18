# Operação de soma: Um problema comum ao solicitar entrada numérica ocorre
# quando as pessoas fornecem texto em vez de números. Quando tentamos
# converter a entrada em um int, recebemos um ValueError. Escreva um
# programa que solicite dois números. Faça a soma deles e exiba o
# resultado. Identifique o ValueError se qualquer valor de entrada não for
# um número e exiba uma mensagem de erro amigável. Teste seu programa
# inserindo dois números e, em seguida, forneça um texto em vez de um
# número.

# Calculadora de soma: Insira o código do Exercício 10.5 em um loop while
# para que o usuário possa continuar fornecendo números, mesmo que cometa
# um erro e insira texto em vez de um número.

while True:
    try:
        num1 = input("insira o numero: ")
        if num1 == 'q':
            break
        num1 = int(num1)
        num2 = input("insira o numero: ")
        if num2 == 'q':
            break
        num2 = int(num2)
    except ValueError:
        print("valor invalido :/")
    else:
        soma = num1 + num2
        print(soma)
