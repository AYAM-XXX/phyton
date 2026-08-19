'''tipo de triangulo'''
# ler 3 entradas de lados de um triangulo e verificar se e um triangulo
# e definit qual o tipo de tianglo
# saber se e triangulo a < b+c, b < a+c, c < a+b
# entrada: lado1,lado2,lado3
# saida : tipo de triangulo

l1 = float(input("digite o lado: "))
while l1 < 0:
    l1 = float(input("digite o lado: "))

l2 = float(input("digite o lado: "))
while l2 < 0:
    l2 = float(input("digite o lado: "))

l3 = float(input("digite o lado: "))
while l3 < 0:
    l3 = float(input("digite o lado: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    if l1 == l2 and l1 == l3:
        print("equilatero")
    elif l1 == l2 or l3 == l1 or l2 == l3:
        print("isoceles")
    else:
        print("escaleno")
else:
    print("triangulo invalido")
