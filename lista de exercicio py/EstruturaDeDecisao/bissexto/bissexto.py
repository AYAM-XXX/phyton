'''ano bisexto'''
# Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.
ano = int(input("digite o ano: "))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print(f"{ano} e bissexto")
else:
    print("não e bissexto")
