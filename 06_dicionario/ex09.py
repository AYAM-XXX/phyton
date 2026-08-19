alunos = []
for x in range(0, 5):
    aluno = {}
    aluno["nome"] = input("insira o  nome do aluno: ")
    aluno["nota"] = float(input("insira a  nota do aluno: "))
    print("")
    alunos.append(aluno)


for aluno in alunos:
    if aluno["nota"] >= 7:
        print(f"nome: {aluno["nome"]}\nnota: {aluno["nota"]}")