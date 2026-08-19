# (Finanças): Uma lista armazena os gastos diários de uma pessoa durante uma
# semana (7 valores). Crie um programa que calcule e mostre a média diária de gastos
# utilizando funções de tamanho e soma.

gastos = []
for x in range(0, 6):
    gasto = float(input("Insira seus gastos diarios: "))
    gastos.append(gasto)

media = sum(gastos) / len(gastos)
print(f"gastos diarios são: {media}")