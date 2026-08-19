# 5. Peça a quantidade de alunos de uma turma e as notas de cada aluno. Ao final,
# calcule a média da turma.

qtd = int(input("Enter quantity of students: "))
grade = 0
sum = 0

for x in range(1, qtd + 1):
    grade = float(input("Enter student grade: "))
    sum += grade

print(f"Avarenge grade clsss: {sum / qtd}")