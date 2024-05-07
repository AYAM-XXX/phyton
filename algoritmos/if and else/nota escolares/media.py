'''calcular media escolar'''
# ler quatro valores de nota escolar de um aluno, e imprimir
# uma msg dizendo se o aluno foi aprovado se a media foi >= 5
# enviar uma mensagem e a media
# entrada: nota, somador
# saida: media

nota = []
soma = 0
exame = []
for x in range(0, 4):
    nota = float(input(f"digite nota {x+1}: "))
    while nota < 0 or nota > 10:
        nota = float(input(f"digite nota {x+1}: "))
    soma = soma + nota
media = soma / 4

if media >= 7:
    print("aprovado")
    print(f"media: {media:.2f}")
else:
    exame = float(input("nota do exame: "))
    while exame < 0 or nota > 10:
        exame = float(input("digite nota: "))
    media = (media + exame) / 2
    if media >= 5:
        print("aprovado")
        print(f"media: {media:.2f}")
    else:
        print("reprovado")
        print(f"media: {media:.2f}")
