aluno = {}

aluno["nome"] = input("insira o nome: ")
aluno["nota1"] = float(input("insira a nota do aluno: "))
aluno["nota2"] = float(input("insira a segunda nota do aluno: "))

media = (aluno["nota1"] + aluno["nota2"]) / 2

print(f"Nome: {aluno["nome"]}")
print(f"Nota 1: {aluno["nota1"]}")
print(f"Nota 2: {aluno["nota2"]}")
print(f"Media: {media}")

if media >= 7:
    print("Situação: APROVADO")
else:
    print("REPROVADO")