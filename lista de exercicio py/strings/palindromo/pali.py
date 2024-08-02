'''Palíndromo'''
# . Um palíndromo é uma seqüência de caracteres cuja leitura é
# idêntica se feita da direita para esquerda ou vice−versa.
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais
# complexos os espaços e pontuação são ignorados. A
# frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma
# onde os espaços foram ignorados. Faça um programa que leia uma
# seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
frase = input("digite a frase: ")
pali = frase.replace(' ', '')
if pali == pali[::-1]:
    print(f"{frase} e um palindromo")
else:
    print(f"{frase} não e um palindromo")
