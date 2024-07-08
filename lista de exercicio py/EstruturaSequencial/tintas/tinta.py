'''calcular tinta'''
# Faça um programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3
# metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas
# de tinta a serem compradas e o preço total.
metros = float(input("digite os metros^2: "))
while metros <= 0:
    metros = float(input("digite os metros^2: "))
price = ((metros / 3) / 18) * 80
pricegl = ((metros / 3) / 3.6) * 25
qtd = ((metros / 3) / 18)
qtdgl = ((metros / 3) / 3.6)
print(f"preço: {price:.2f} R$\nlatas: {int(qtd)}\ngalões: {int(qtdgl)}\npreço galão: {pricegl:.2f} R$")
