''' salario liquido'''
# construir um prgama que efetur o calculo do sálaio liquido de
# um professir .Para fazer este progama você deverá possuir alguns
# dados , tais como: valor da hora aula, numero de aulas dadas no mes
# e percentual de desconto do INSS .Em primeiro lugar , deve-se
# estabelecer qual será o seu salario  bruto para efetuar o
# desconto  e ter o valor salario liquido

# entradas: float(hora aula), int(numero de aulas), int(desconto)
# saida : float(salario bruto)

ValorHora = input("Valor da hora: ")
QtdHoras = input("Quantidade hora: ")
Dsct = input("Valor desconto: ")
SalarioLiquido = float(ValorHora) * float(QtdHoras) * ((1 - float(Dsct) / 100))
print(SalarioLiquido)
