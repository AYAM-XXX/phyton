"""calculador de volume"""
# calcular e apresentar  o valor do volume de uma  lata de oleo
# formula <-- 3.14159 * r^2 * altura
# entradas: floar(raio), float(altura)
# saida: float(volume)

raio = float(input("valor do raio:"))
while raio < 0:
    raio = float(input("valor do raio:"))
altura = float(input("valor altura: "))
while altura < 0:
    altura = float(input("valor altura: "))
volume = 3.14159 * raio**2 * altura
print(f"volume da lata: {volume:.2f}")
