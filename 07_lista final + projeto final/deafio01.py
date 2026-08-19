
numeros  = []
for x in range(0,15):
    numeros.append(int(input("insira um numero: ")))

maior = float("-inf")
menor = float("inf")
for num in numeros:
    if maior < num:
        maior = num
    if menor > num:
        menor = num


print(f"maior: {maior}")
print(f"menor: {menor}")

