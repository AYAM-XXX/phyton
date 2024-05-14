# ler os dados de um vetor A e passar para um vetor B multplicando por 3
vetA = []
vetB = []
for x in range(8):
    vetA.append(int(input("digite o valor: ")))
    vetB.append(vetA[x] * 3)
print("vetor A")
for x, item in enumerate(vetA):
    print(f"indice[{x}] valor: {item}")
print("vetor B")
for x, item in enumerate(vetB):
    print(f"indice[{x}] valor: {item}")
