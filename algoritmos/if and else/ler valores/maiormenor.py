'''ler 5 valores e ver qual e o menor e o maior'''
valor = []
maior = 0
menor = 0
for x in range(0, 5):
    valor = int(input("digite um valor: "))
    if x == 0:
        maior = valor
        menor = valor
    else:
        if maior < valor:
            maior = valor
        elif menor > valor:
            menor = valor
print(f"maior valor: {maior}\nmenor valor: {menor}")
