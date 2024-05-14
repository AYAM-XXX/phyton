'''somar numeros matriz'''
# fazer uma matriz que leia 5 elementos e some todos os valores impar
# entrada: vetA, soma
vetA = []
soma = 0
for x in range(5):
    vetA.append(int(input("digite um valor: ")))
    if vetA[x] % 2 != 0:
        soma = soma + vetA[x]
print(f"soma: {soma}")
