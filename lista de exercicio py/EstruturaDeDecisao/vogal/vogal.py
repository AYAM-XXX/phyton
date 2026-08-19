'''verifica se e vogal'''
#  Faça um Programa que verifique se uma letra digitada é
#  vogal ou consoante.

letra = input("digite a letra: ")
if letra: 
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print("A letra e uma vogal")
    else:
        print("A letra e uma consoante")
else:
    print("digitou errado")