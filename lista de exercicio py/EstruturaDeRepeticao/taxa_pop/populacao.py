'''escrever um pograma que calcule a taxa de crescimento'''
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
# número de anos necessários para que a população do país A ultrapasse ou iguale 
# a população do país B, mantidas as taxas de crescimento.
ano = 0
cidade_a = 80000
cidade_b = 200000
while cidade_a <= cidade_b:
    cidade_a = cidade_a + (cidade_a * 0.03)
    cidade_b = cidade_b + (cidade_b * 0.015)
    ano += 1
print(f'cidade A levara {ano} para ser maior que a cidade B')
print(f'população cidade A: {int(cidade_a)}')
print(f'população cidade B: {int(cidade_b)}')