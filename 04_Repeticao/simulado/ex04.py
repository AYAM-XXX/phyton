# Uma indústria alimentícia realiza inspeções periódicas em sua linha de produção. Cada
# lote produzido recebe uma nota de qualidade variando de 0 a 10, atribuída pelo inspetor
# responsável.
# Como o número de lotes avaliados varia diariamente, decidiu-se que o sistema deverá
# continuar registrando notas até que o inspetor informe -1, indicando o encerramento da
# inspeção.
# Desenvolva um programa que apresente, ao final:
# • quantidade de lotes avaliados;
# • média das notas;
# • maior nota registrada;
# • menor nota registrada.
# Caso nenhuma nota válida seja informada, o programa deverá exibir uma mensagem
# apropriada.
import sys

largest = 0
lower = sys.maxsize
avarenge = 0
grade = 0
qtd = 0
while True:
    grade = int(input(f" Enter grade: "))
    if grade == -1:
        break
    while grade < -1 or grade > 10:
        grade = int(input(f" Enter grade again: "))
    if largest < grade:
        largest = grade
    if lower > grade:
        lower = grade

    avarenge += grade
    qtd += 1

print(f"Quantity of test: {qtd}")
print(f"Avarenge age: {avarenge / 25}")
print(f"largest grade reported: {largest}")
print(f"Lower grade reported: {lower}")