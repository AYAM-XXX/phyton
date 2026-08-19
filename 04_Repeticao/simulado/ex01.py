# Nos últimos anos, o aumento do consumo de energia elétrica levou diversas
# concessionárias a adotarem mecanismos para incentivar o uso consciente dos recursos
# energéticos. Em uma dessas concessionárias, o valor da conta é calculado com base no
# consumo mensal do cliente, podendo haver cobrança de uma taxa adicional para
# consumidores que ultrapassam determinado limite de consumo.
# Considere as seguintes regras:
# • Valor do kWh: R$ 0,85;
# • Caso o consumo seja superior a 250 kWh, acrescentar uma taxa fixa de R$
# 30,00.
# Desenvolva um programa que receba o consumo mensal de um cliente e apresente:
# • consumo informado;
# • valor total da conta

kwh = int(input("Enter kwh: "))
if(kwh > 250):
    print(f"Total energy usage: {kwh}\n Total price: {(kwh * 0.85) + 30}R$")
    print("Charged rate: 30R$")
else:
    print(f"Total energy usage: {kwh}\n Total price: {(kwh * 0.85)}R$")