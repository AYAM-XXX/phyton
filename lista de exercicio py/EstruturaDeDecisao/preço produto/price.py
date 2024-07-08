'''recomendar o produto mais barato'''
# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato
prod_1 = float(input("digite o preço do produto: "))
prod_2 = float(input("digite o preço do produto: "))
prod_3 = float(input("digite o preço do produto: "))
if prod_1 < prod_2 and prod_1 < prod_3:
    print(f"produto mais barato: {prod_1:.2f}")
elif prod_2 < prod_1 and prod_2 < prod_3:
    print(f"produto mais barato:  {prod_2:.2f}")
else:
    print(f"produto mais barato: {prod_3:.2f}")
