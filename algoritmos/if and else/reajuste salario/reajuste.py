'''reajusta salario de funcionarios'''
# reajusta o salario do funcionario considerando que se um
# funcionario ganhar menos que 500 reajuste sera 15%
# funcionario ganhar mais do 1ue 500 ate 1000 reajuste 10%
# funcionario ganhar mais do que 1000 reajuste sera 5%
# entrada:  float(salario)
# saida: float(salario_novo)
salario = float(input("qual o salrio: "))
while salario < 100:
    salario = float(input("qual o salrio: "))
reajuste = 0

if salario < 500:
    reajuste = salario + (salario * 0.15)
elif salario <= 1000:
    reajuste = salario + (salario * 0.10)
else:
    reajuste = salario + (salario * 0.05)
print(f'salario atual: {reajuste:.2f}')
