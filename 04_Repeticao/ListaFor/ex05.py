# 5.Crie um script que percorra uma lista de números inteiros de sua escolha e exiba ao
# final qual era o menor número contido na lista e qual era o maior deles.

lista = [1,2,3,7,5,3,2,56,7,89,4,2,1,5,7,8,98,3,4,5,6,7,8,9,0,2,3,5,45,66,7,58,5,85,5,4,34,35,23]

maior = 0
menor = 0
for x in range(len(lista)):
    if x == 0:
        maior = lista[x]
        menor = lista[x]
    else:
        if maior < lista[x]:
            maior = lista[x]
        if menor > lista[x]:
            menor = lista[x]

print(f"maior: {maior}\nmenor: {menor}")