# ler uma matriz 3x3 e conta os pares
matriz = []
cont = 0
for x in range(3):
    linha = []
    for z in range(3):
        msg = int(input("digite um numero:"))
        linha.append(msg)
        if msg % 2 == 0:
            cont += 1
    matriz.append(linha)
print(f"numero de pares: {cont}")
for x in range(3):
    print(matriz[x])
