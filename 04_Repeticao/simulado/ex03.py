# Uma prefeitura pretende ampliar os projetos esportivos oferecidos à população. Antes
# de definir quais atividades serão disponibilizadas, foi realizado um levantamento para
# conhecer o perfil etário dos participantes inscritos.
# O sistema deverá receber a idade de 25 participantes e, ao final da coleta, gerar um
# relatório contendo:
# • quantidade de menores de idade;
# • quantidade de maiores de idade;
# • média das idades;
# • maior idade informada;
# • menor idade informada.
import sys

largest_age = 0
lower_age = sys.maxsize
minors = 0
adults = 0
avarenge = 0
for i in range(0, 25):
    age = int(input(f"{i + 1} Enter age: "))
    if largest_age < age:
        largest_age = age
    if lower_age > age:
        lower_age = age
    if age >= 18:
        adults += 1
    else:
        minors += 1
    avarenge += age

print(f"quantity minors age: {minors}")
print(f"quantity adults age: {adults}")
print(f"Avarenge age: {avarenge / 25}")
print(f"oldest age reported: {largest_age}")
print(f"youngest age reported: {lower_age}")