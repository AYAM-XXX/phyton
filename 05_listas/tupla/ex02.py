# 2. Análise de Tupla Numérica
# Crie uma tupla com 5 números inteiros digitados pelo usuário (use um loop para
# ler). Depois, exiba:
# • O maior número.
# • O menor número.
# • A soma de todos os valores.
num = []
for x in range(0, 5):
    num.append(int(input("digite um numero: ")))
tupla = (num[0], num[1], num[2], num[3], num[4])

print(f"maior numero: {max(tupla)}\n menor numero: {min(tupla)}\nsoma: {sum(tupla)}")