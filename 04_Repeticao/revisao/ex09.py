# 9. Solicite um número inteiro positivo e calcule seu fatorial.

num = int(input("Enter num: "))

def fatorial(num):
   if num == 1:
       return 1
   return num * fatorial(num - 1)

print(f"factorial: {fatorial(num)}")