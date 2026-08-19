distancia = int(input("Digite o valor de distancia: "))
precoGasolina = float(input("digite o preço da gasolina: "))
litrosDistancia = 12
precoTotal =  (distancia/litrosDistancia) * precoGasolina
print(f"litros de gasolina que o carro vai consumuir: {(distancia/litrosDistancia):.2f} litros\n preço total gasto: {precoTotal:.2f}")