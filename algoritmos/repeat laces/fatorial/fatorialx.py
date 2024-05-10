'''fatorial de um numero'''
# fazer o fatorial de algum numero
# entrada: int(nmr)
# saida: fat
nmr = int(input("digite um numero: "))
fat = 1
for x in range(0, nmr):
    fat = fat * (x + 1)
print(fat)
