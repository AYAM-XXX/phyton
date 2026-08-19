'''jogo da forca'''
#  Jogo de Forca. Desenvolva um jogo da forca. O programa terá
# uma lista de palavras lidas de um arquivo texto e escolherá
# uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

frase = input("digite a frase: ")
palavra = ['_'] * len(frase)
erros = 6
acertos = 0
while erros != 0 or acertos == len(frase):
    tent = input("digite a frase: ")

    if tent in frase:
        for x in range(len(frase)):
            if tent == frase[x]:
                palavra[x] = tent
                acertos += 1

        print(str(palavra))
    else:
        erros -= 1
        print(f"palavra não encontrada\ntentativas: {erros}")
