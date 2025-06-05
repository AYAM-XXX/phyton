# Um loja oferece descontos em compras com base no valor total:
# • Até R$ 100,00: sem desconto.
# • De R$ 100,01 a R$ 500,00: 10% de desconto.
# • Acima de R$ 500,00: 20% de desconto.
# Escreva um programa que leia o valor da compra e o tipo de cliente
# ("Comum" ou "VIP"). Clientes VIP recebem um desconto adicional de
# 5% sobre o valor final (após o desconto inicial).
# Exiba o valor final a pagar.

def desconto(valor, cliente):
    if valor > 100 and valor <= 500:
        if cliente == "VIP":
            valor = valor * 0.85
        else:
            valor = valor * 0.90
    elif valor > 500:
        if cliente == "VIP":
            valor = valor * 0.75
        else:
            valor = valor * 0.80
    return valor


def validador_de_cliente(cliente):
    if cliente == "1" or cliente == "2":
        return True
    else:
        return False


def valor_do_produto():
    while True:
        print("insira o valor do produto: ")
        valor = input("digite: ")
        try:
            valor = float(valor)
            break
        except ValueError:
            print("valor incorreto")
    return valor


def cliente_tipo():
    while True:
        print("qual o tipo do cliente:\n1- vip\n2- comum")
        cliente = input("digite: ")
        validador = validador_de_cliente(cliente)
        if validador == True:
            
            break
        else:
            print("valor inserido errado")
    return cliente


valor = valor_do_produto()
cliente = cliente_tipo()
preco_final = desconto(valor, cliente)
print(f"preço final da compra: {preco_final}R$")
