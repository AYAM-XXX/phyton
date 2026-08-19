meses_do_ano = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

entrada = int(input("digite o mes que deseja pesquisar: "))
while entrada < 0 and entrada > 12:
    entrada = int(input("digite o mes que deseja pesquisar de 1 a 12: "))

for x in range(len(meses_do_ano)):
    if (entrada -1) == x:
        print(meses_do_ano[x])