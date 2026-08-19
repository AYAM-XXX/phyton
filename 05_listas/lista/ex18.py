# (Hotelaria): Um hotel armazena a idade de seus hóspedes atuais em uma lista.
# Escreva um programa que use um laço para exibir apenas as idades das pessoas que
# forem maiores de idade (18 anos ou mais).

idades = [
    12, 15, 18, 19, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
    47, 48, 49, 50, 52, 54, 55, 58, 60, 62,
    65, 68, 70, 72, 75, 78, 80, 82, 85, 88
]

for idade in idades:
    if idade >= 18:
        print(idade)