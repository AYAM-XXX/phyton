# 3. Peça 10 números ao usuário e informe:
# o Quantos são positivos;
# o Quantos são negativos;
# o Quantos são iguais a zero.
positive = 0
negative = 0
equals_zero = 0
for x in range(1, 11):
    num = int(input("Enter a number: "))
    if num == 0:
        equals_zero += 1
    if num < 0:
        negative += 1
    if num > 0:
        positive += 1

print(f"negative numbers: {negative}\npositive numbers: {positive}\nEquals zero: {equals_zero}")

