''' diagrama em blocos'''
# ler quatro numeros e apresentar o resultado em adição em
# multiplicação, baseado-se na proprieadade de distribuição,
# no caso devera ser distruibuido A,B,C,D ex : A*B, A*C, A*D
# entrada: entrA , entrB, entrC , entrD
# saida: em diagrama

entrA = input("digite um valor")
entrB = input("digite um valor")
entrC = input("digite um valor")
entrD = input("digite um valor")

print(" distribuição A")
print(int(entrA) + int(entrB))
print(int(entrA) * int(entrB))

print(int(entrA) + int(entrC))
print(int(entrA) * int(entrC))

print(int(entrA) + int(entrD))
print(int(entrA) * int(entrD))

print(" distribuição B")
print(int(entrB) + int(entrC))
print(int(entrB) * int(entrC))
print(int(entrB) + int(entrD))
print(int(entrB) * int(entrD))

print(" distribuição C")
print(int(entrC) + int(entrD))
print(int(entrC) * int(entrD))
