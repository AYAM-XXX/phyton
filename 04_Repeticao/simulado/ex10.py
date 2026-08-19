# Questão 10 – Sistema de Avaliação Física
# (2,0 pontos)
# Uma rede de academias deseja desenvolver um sistema para auxiliar os professores na
# avaliação inicial de novos alunos.
# O programa deverá permitir o cadastro de vários alunos. Para cada aluno deverão ser
# informados:
# • nome;
# • idade;
# • peso (kg);
# • altura (m).
# O sistema deverá calcular o Índice de Massa Corporal (IMC), utilizando a fórmula:
# �
# �𝑀𝐶 = peso
# altura2
# Em seguida, o aluno deverá ser classificado conforme a tabela:
# IMC
# Menor que 18,5
# Entre 18,5 e 24,9
# Entre 25 e 29,9
# Classificação
# Abaixo do peso
# Peso normal
# Sobrepeso
# Igual ou superior a 30 Obesidade
# O programa deverá continuar cadastrando alunos até que o usuário escolha encerrar.
# Ao final, apresente:
# • quantidade total de alunos cadastrados;
# • média das idades;
# • maior IMC calculado;
# • menor IMC calculado;
# • quantidade de alunos classificados em cada faixa de IMC;

import sys

greater_weight = 0
imc_greater = 0
imc_normal = 0
lower_weight = sys.maxsize
weight = 0
avarenge = 0
qtd = 0
sum_age = 0
imc_lower = 0
while True:
    name = input("Enter name:  ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight: "))
    size = float(input("Enter size: "))
    imc = weight / (size**2)
    if greater_weight < imc:
        greater_weight = imc
    if lower_weight >  imc:
        lower_weight = imc
    if imc <= 18.5:
        imc_lower += 1
        print("weight under of normal")
    elif imc > 18.5 and imc < 30:
        imc_normal += 1
        print("normal weight")
    else:
        imc_greater += 1
        print("weight above of normal")
    qtd += 1
    sum_age += age
    choice = int(input("User wish register another book? 1- yes/2- no: "))
    if choice == 1:
        continue
    else:
        break


print(f"quantity of students : {qtd}")
print(f"avarenge of age: {sum_age / qtd}")
print(f"Greater imc: {greater_weight}")
print(f"lower imc: {lower_weight}")
print(f" Under weight: {imc_lower}")
print(f" Normal weight: {imc_normal}")
print(f" Above weight: {imc_greater}")