'''ler numeros divisiveis por 2 e 3'''
# ler 4 numeros inteiros e efetuar e ver divisiveis por 2 e 3
n1 = int(input("insira um valor: "))
n2 = int(input("insira um valor: "))
n3 = int(input("insira um valor: "))
n4 = int(input("insira um valor: "))
if n1 % 2 == 0 or n1 % 3 == 0:
    print(f"valor divisivel por 2 e 3: {n1}")
if n2 % 2 == 0 or n2 % 3 == 0:
    print(f"valor divisivel por 2 e 3: {n2}")
if n3 % 2 == 0 or n3 % 3 == 0:
    print(f"valor divisivel por 2 e 3: {n3}")
if n4 % 2 == 0 or n4 % 3 == 0:
    print(f"valor divisivel por 2 e 3: {n4}")
