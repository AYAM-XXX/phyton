# Soma e multiplicação de lambdas
# Escreva um programa em Python para criar uma função lambda que adicione
# 15 a um determinado número passado como argumento. Crie também uma função
# lambda que multiplique o argumento x pelo argumento y e imprima o resultado.
# Saída de exemplo:
# 25
# 48

soma = lambda x : x + 15
print(soma(30))

multi = lambda x, y : x * y
print(multi(4, 5))
# Gerador de funções Lambda
# Escreva um programa em Python para criar uma função que recebe um argumento,
# e esse argumento será multiplicado por um número desconhecido fornecido.
# Saída de exemplo:
# Dobrar o número de 15 = 30
# Triplicar o número de 15 = 45
# Quadruplicar o número de 15 = 60
# Quintuplicar o número 15 = 75


def multi_desc(numero):
    return lambda x: x * numero


multi_closure = multi_desc(2)

print(multi_closure(16))
