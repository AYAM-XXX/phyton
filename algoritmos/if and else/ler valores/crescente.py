'''crescente'''
# ler 3 valores e organizar em ordem crescente
Valor_One = int(input("digite o valor: "))
Valor_Two = int(input("digite o valor: "))
Valor_Three = int(input("digite o valor: "))

if Valor_One > Valor_Two and Valor_One > Valor_Three:
    if Valor_Two > Valor_Three:
        print(Valor_Three, Valor_Two, Valor_One)
    else:
        print(Valor_Two, Valor_Three, Valor_One)
elif Valor_Two > Valor_One and Valor_Two > Valor_Three:
    if Valor_One > Valor_Three:
        print(Valor_Three, Valor_One, Valor_Two)
    else:
        print(Valor_One, Valor_Three, Valor_Two)
else:
    if Valor_One > Valor_Two:
        print(Valor_Two, Valor_One, Valor_Three)
    else:
        print(Valor_One, Valor_Two, Valor_Three)
