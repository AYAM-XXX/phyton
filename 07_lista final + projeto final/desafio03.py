alunos = []
for x in range(0,5):
    aluno = {}
    aluno["nome"] = input("indique o nome do aluno: ")
    aluno["idade"] = int(input("indique a idade do aluno: "))
    aluno["nota"] = float(input("indique a nota do aluno: "))
    alunos.append(aluno)

for aluno in alunos:
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
maior_nota = max(alunos, key=lambda aluno : aluno["nota"])
maior_idade = max(alunos, key=lambda aluno : aluno["idade"])
print(f"\nmaior nota: {maior_nota}")
print(f"maior nota: {maior_idade}")
