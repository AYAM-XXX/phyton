"""calcular o custo do coelho"""
# calcular o custo do coelho com base na formula
# custo numero de (coelho * 0.70) / 18 + 10

coelho = int(input("numero de coelho: "))
custo = (float(coelho) * 0.70) / 18 + 10
print(f"custo por coelho: {custo:.2f} R$")
