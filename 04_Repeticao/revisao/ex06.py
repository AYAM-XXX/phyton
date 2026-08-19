# 6. Solicite 10 números e informe o maior e o menor valor digitado.
import sys
largest = 0
lower = sys.maxsize
num = 0
for x in range(1, 11):
    num = int(input(f" Enter num: "))
    if largest < num:
        largest = num
    if lower > num:
        lower = num

print(f"Lowest number: {lower}")
print(f"Largest number: {largest}")
