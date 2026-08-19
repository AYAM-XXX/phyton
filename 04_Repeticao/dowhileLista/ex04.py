# 4.Desenvolva um programa que peça uma sequência de notas de avaliações de um
# projeto técnico. Após inserir cada nota, pergunte se o avaliador quer inserir outra. Se ele
# disser que não, encerre e imprima a maior nota informada.

largest = 0
while True:
    grade = float(input("Enter grade:"))
    if(largest < grade):
        largest = grade
    answer = int(input("u want insert more grade: 1- yes / 2- no: "))
    if answer == 2:
        print(f"Largest grade is {largest}")
        break
    else:
        continue