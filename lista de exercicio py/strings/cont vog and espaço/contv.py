'''Conta espaços e vogais'''
# Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.
frase = input("digite a frase: ")
cont_vogal = 0
cont_branco = 0
for x in range(len(frase)):
    if frase[x] == 'a' or frase[x] == 'e' or frase[x] == 'i' or frase[x] == 'o' or frase[x] == 'u':
        cont_vogal += 1
    if frase[x] == ' ':
        cont_branco += 1

print(f"espaços em branco: {cont_branco}")
print(f"vogais : {cont_vogal}")
