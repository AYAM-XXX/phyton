'''leitand de letras'''
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.
lt = []
consoante = []
cont = 0
for x in range(10):
    lt.append(input("digite um caracter: "))
    if lt[x] != 'a' and lt[x] != 'e' and lt[x] != 'i' and lt[x] != 'o' and lt[x] != 'u':
        consoante.append(lt[x])
        cont += 1
    else:
        pass
print(f'consoantes: {consoante}\n quantidade: {cont}')
