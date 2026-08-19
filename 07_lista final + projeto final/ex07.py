numeros = []
for x in range(0, 10):
    num = int(input("digite o numero: "))
    if num % 2 == 0:
        numeros.append(num)

print(numeros)
print(f"total de numeros pares: {len(numeros)}")