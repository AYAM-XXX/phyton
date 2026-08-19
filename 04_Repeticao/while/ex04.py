# 4.Crie um programa que funcione como um simulador simples de poupança: pergunte
# o valor inicial investido, o rendimento mensal fixo em porcentagem (ex: 1%) e exiba
# quanto dinheiro estará na conta mês a mês durante o primeiro ano (12 meses).
deposit = float(input("Enter initial deposit: "))
while deposit < 0:
    deposit = float(input("Enter initial deposit correctly: "))
rate = float(input("Enter interest rate: "))
while deposit < 0:
    rate = float(input("Enter interest rate correctly: "))
print(f"one year, the earning will be {deposit * (rate / 100)}")