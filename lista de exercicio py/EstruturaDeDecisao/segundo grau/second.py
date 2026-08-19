import math
'''equação do segundo grau'''
valor_a = int(input("insira o valor de A: "))
if valor_a != 0:
    valor_b = int(input("insira o valor de B: "))
    valor_c = int(input("insira o valor de C: "))
    delta = (valor_b ** 2) - (4 * valor_c * valor_a)
    if delta < 0:
        print("não possui raizes reais")
    elif delta == 0:
        print(f"raiz: {((-1) * valor_b) / (2 * valor_a)}")
    else:
        print(
            f"raizes\n x': {(((-1) * valor_b) + math.sqrt(delta)) / (2 * valor_a)}")
        print(f"x'': {(((-1) * valor_b) - math.sqrt(delta)) / (2 * valor_a)}")
else:
    pass
