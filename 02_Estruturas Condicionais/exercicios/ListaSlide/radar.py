velocidade = int(input("digite a velocidade: "))
if(((velocidade * 1.20) > 100) and velocidade < 120):
    print("recebeu multa media")
elif((velocidade) > 120):
    print("recebeu multa grave")
else:
    print("não recebeu multa")










# radar de Velocidade Inteligente: Um radar emite multas severas se o motorista passar a mais de 20% acima
# do limite permitido da via (100 km/h). Escreva um script que diga se o motorista não foi multado, se
# recebeu multa média (até 120 km/h) ou multa grave (acima de 120 km/h).