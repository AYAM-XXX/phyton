'''define o turno'''
# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#  ou "Valor Inválido!", conforme o caso.
turno = input("digite seu turno: ")
if turno == "m" or turno == "M":
    print("bom dia")
elif turno == "V" or turno == "v":
    print("boa tarde")
elif turno == "n" or turno == "N":
    print("boa noite")
else:
    print("valor incorreto")
