'''tabuada com while'''
# informe um numero e faça a tabuada desse numero
# entrada: int(nmr)
nmr = int(input("insira um numero: "))
cont = 0
while cont <= 10:
    print(f"{nmr} x {cont} = {nmr * cont}")
    cont = cont + 1
