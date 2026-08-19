numeros = []

for x in range(0, 8):
    num = int(input("insira um numero: "))
    numeros.append(num)

print(f"\n"
      f"maior numero: {max(numeros)}\n"
      f"menor numero: {min(numeros)}\n"
      f"soma de todos os numeros: {sum(numeros)}")