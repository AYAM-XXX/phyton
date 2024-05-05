''' converter temperatura de fahrenheit  para celsius'''
# ler uma temperatura em fahrenheit e tranforma pela formula
# c <-- (f - 32) * (5 / 9)
# entrada: fahrenheit
# saida: celsius

fahrenheit = float(input("qual a temperatura: "))
celsius = (fahrenheit - 32) * (5 / 9)
print(f"temperatura em celsius: {celsius:.2f}")
