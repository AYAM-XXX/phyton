# 4. Solicite a idade de 15 pessoas e informe:
# o Quantos são maiores de idade;
# o Quantos são menores de idade.

import sys

largest_age = 0
lower_age = sys.maxsize
minors = 0
adults = 0
for i in range(1, 16):
    age = int(input(f"Enter age: "))
    if age >= 18:
        adults += 1
    else:
        minors += 1

print(f"quantity minors age: {minors}")
print(f"quantity adults age: {adults}")
