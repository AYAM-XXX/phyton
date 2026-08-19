'''hipermecado'''
# O Hipermercado Tabajara está com uma promoção de carnes que é
# imperdível.
# Confira:
#  Até 5 Kg Acima de 5 Kg
# File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
# Picanha R$ 6,90 por Kg R$ 7,80 por Kg
cart = 0
kg = int(input("quantidade de kg: "))
print("fl - file duplo\nal - alcatra\npi - picanha")
esc = input("digite: ")
print("compra com cartão?\ns - sim\nn - não")
id = input("digite: ")
if id == 's':
    cart = 0.05
else:
    pass
if esc == "fl":
    if kg <= 5:
        print(f"preço: R$ {(kg * 5.80) - (kg * 5.80 * cart):.2f}")
    else:
        print(f"preço: R$ {(kg * 4.90) - (kg * 4.90 * cart):.2f}")
elif esc == "al":
    if kg <= 5:
        print(f"preço: R$ {(kg * 6.80)  - (kg * 6.80 * cart):.2f}")
    else:
        print(f"preço: R$ {(kg * 5.90) - (kg * 5.90 * cart):.2f}")
elif esc == "pi":
    if kg <= 5:
        print(f"preço: R$ {(kg * 7.80) - (kg * 7.80 * cart):.2f}")
    else:
        print(f"preço: R$ {(kg * 6.90) - (kg * 6.90 * cart):.2f}")
else:
    print("erro")
