# Múltiplos de dez: Solicite ao usuário um número e informe se
# o número é múltiplo de 10 ou
# não.

prompt = "insira um numero: "
num = input(prompt)
num = int(num)
if num % 10 == 0:
    print("esse numero é multiplo de 10")
else:
    print("esse numero não é multiplo de 10")
