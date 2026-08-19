alunos = []
tam = 3
media = 0
maior = float("-inf")
nome = ""
for x in range(0, tam):
    aluno = {}
    aluno["nome"] = input("insira o nome: ")
    aluno["nota"] = float(input("insira a nota: "))
    alunos.append(aluno)

for item in alunos:
    media += item["nota"]
    if item["nota"] > maior:
        maior = item["nota"]
        nome = item["nome"]

media = media / tam

for item in alunos:
    print(f"nome: {item["nome"]}")

print(f"media da turma: {media:.2f}")
print(f"aluno com maior nota {nome}\nmaior nota: {maior}")