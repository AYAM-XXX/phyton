'''analisa se é decimal'''
# Faça um Programa que peça um número e informe se o número é
# inteiro ou decimal.
nmr = float(input("digite o numero: "))
if nmr.is_integer():
    print(f"{nmr} e inteiro")
else:
    print(f"{nmr} e decimal")
