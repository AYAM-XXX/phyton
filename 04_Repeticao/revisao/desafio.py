# Desafio – Sistema de Cadastro e
# Estatísticas de Alunos
# Uma escola deseja realizar um levantamento sobre o desempenho de seus alunos.
# Desenvolva um programa que permita cadastrar vários alunos. O programa deverá
# continuar solicitando dados até que o usuário escolha encerrar o cadastro.
# Para cada aluno, informe:
# • Nome do aluno;
# • Idade;
# • Nota final (0 a 10).
# Ao final, o programa deverá exibir:
# 1. Quantidade total de alunos cadastrados;
# 2. Média geral das notas;
# 3. Maior nota informada;
# 4. Menor nota informada;
# 5. Quantidade de alunos aprovados (nota maior ou igual a 6);
# 6. Quantidade de alunos reprovados;
# 7. Percentual de aprovados;
# 8. Percentual de reprovados.

students = []

print("=== Student Registration System ===")

while True:
    name = input("Enter student name (or press Enter to finish): ").strip()
    if name == "":
        break

    age = int(input("Enter age: "))
    grade = float(input("Enter final grade (0 to 10): "))

    students.append({"name": name, "age": age, "grade": grade})

if len(students) == 0:
    print("\nNo students registered.")
else:
    total_students = len(students)
    sum_grades = 0
    highest_grade = students[0]["grade"]
    lowest_grade = students[0]["grade"]
    passed_count = 0

    for student in students:
        grade = student["grade"]
        sum_grades += grade
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade
        if grade >= 6:
            passed_count += 1

    failed_count = total_students - passed_count
    avg_grade = sum_grades / total_students
    passed_percentage = (passed_count / total_students) * 100
    failed_percentage = (failed_count / total_students) * 100

    print("\n=== Statistics ===")
    print("Total students:", total_students)
    print("Average grade:", round(avg_grade, 2))
    print("Highest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)
    print("Passed students:", passed_count)
    print("Failed students:", failed_count)
    print("Pass percentage:", round(passed_percentage, 2), "%")
    print("Fail percentage:", round(failed_percentage, 2), "%")
