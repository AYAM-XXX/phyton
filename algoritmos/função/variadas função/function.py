'''tipos variados de função'''
# variedade de função
tam = 2
matrizA = []
matrizB = []
matrizC = []


def somatorio(n):
    soma = 0
    for x in range(n + 1):
        soma += x
    return soma


def lermatrizA(matriz):
    for x in range(tam):
        lista = []
        for y in range(tam):
            valor = int(input("insira um valor matriz A: "))
            lista.append(valor)
    matriz.append(lista)


def lermatrizC():
    for x in range(tam):
        lista = []
        for y in range(tam):
            valor = matrizA[x][y] + matrizB[x][y]
            lista.append(valor)
        matrizC.append(lista)


def ordena(matriz):
    for x in range(tam):
        for y in range(tam):
            for z in range(tam):
                if matriz[x][y] < matriz[x][z]:
                    matriz[x][y], matriz[x][z] = matriz[x][z], matriz[x][y]


def lermatrizB(matriz):
    for x in range(tam):
        lista = []
        for y in range(tam):
            valor = int(input("insira um valor matriz B: "))
            lista.append(valor)
    matriz.append(lista)


def mostrar(matriz):
    for x in range(tam):
        for y in range(tam):
            print(matriz[x][y])
        print("\n")


lermatrizA(matrizA)
lermatrizB(matrizB)
lermatrizC()
ordena(matrizA)
ordena(matrizB)
ordena(matrizC)
print("\n MATRIZ A\n")
mostrar(matrizA)
print("\n MATRIZ B\n")
mostrar(matrizB)
print("\n MATRIZ C\n")
mostrar(matrizC)

# define uma taxa de atraso
# def atraso(valor, taxa, tempo):
#     prest = valor + (valor * (taxa / 100) * tempo)
#     return print(prest)


# atraso(200, 10, 3)
