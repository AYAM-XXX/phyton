dias_da_semana = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
)

entrada = int(input("digite o dia da semana que deseja pesquisar: "))
while entrada < 1 and entrada > 7:
    entrada = int(input("digite o dia da semana que deseja pesquisar de 1 a 7: "))

for x in range(len(dias_da_semana)):
    if (entrada -1) == x:
        print(dias_da_semana[x])