'''temperatura cada mes'''
# Faça um programa que receba a temperatura média de cada mês do ano
# e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
# e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temp = []
soma = 0
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
for x in range(12):
    temp.append(float(input("digite a temperatura: ")))
    soma += temp[x]

for x in range(12):
    print(f'{x + 1} - {mes[x]}: {temp[x]}º')
print(f'temperatura media: {soma / 12}')
