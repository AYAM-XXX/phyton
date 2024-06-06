# ler uma matriz 3x3 e conta os pares
matriz = []
cont = 0
for x in range(3):
    linha = []
    for z in range(3):
        msg = int(input("digite um numero:"))
        linha.append(msg)
    matriz.append(linha)
    for linha in matriz:
        for e in linha:
            if e % 2 == 0:
                cont += 1
print(f"numero de pares: {cont}")
for x in range(3):
    print(matriz[x])
