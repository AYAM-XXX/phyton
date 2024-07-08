'''verifica o sexo'''
#  Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
sexo = input("digite o sexo: ")
if sexo == "M" or sexo == "m":
    print("masculino")
elif sexo == "F" or sexo == "f":
    print("feminino")
else:
    print("sexo invalido")
