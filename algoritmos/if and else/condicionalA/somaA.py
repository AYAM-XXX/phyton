'''condicionalA'''
# verificar se a soma de 2 variaveis e maior igual a 10
# se for soma mais 5 se não subtrai 7

varA = int(input("digite um numero: "))
varB = int(input("digite um numero: "))
soma = varA + varB
if soma >= 10:
    soma = soma + 5
else:
    soma = soma - 7
print(soma)
