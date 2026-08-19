# 2. Solicite um número ao usuário e exiba sua tabuada de 1 a 10.
num = int(input("Enter num: "))
for x in range(1, 11):
    print(f"{x} x {num} = {num * x}")
