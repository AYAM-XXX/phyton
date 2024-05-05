'''gasto combustivel'''
# um automovel faz 12 km por litro , faça um progama que calcula
# a quantidade de combustivel gasto , com as entradas de tempo e km/h
# pegue a distancia e ache faça o calculo do combustivel
# constante : 12km por litro
# entradas: tempo , kmh
# saida: distancias, gasto

tempo = float(input("tempo percorrido: "))
kmh = float(input("km/h: "))
distancia = tempo * kmh
print("consumo de gasolina: {:.2f}".format(distancia / 12))
