"""boleto atrasado"""
# efetuar a opeação de uma prestação atrasada
# VALOR + (VALOR * TAXA/100 * TEMPO)
# entrada: valor, taxa * tempo
# saida: prestação

valor = float(input("valor da fatura: "))
while valor < 0:
    valor = float(input("valor da fatura: "))
taxa = float(input("valor da taxa: "))
while taxa < 0:
    taxa = float(input("valor da taxa: "))
tempo = float(input("quantidades dias atrasados: "))
while tempo < 0:
    tempo = float(input("quantidades dias atrasados: "))
total = valor + (valor * (taxa/100) * tempo)
print(f"total da prestação: {total:.2f}")
