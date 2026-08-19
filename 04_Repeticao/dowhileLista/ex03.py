# 3.Crie um sistema de cadastro onde o usuário insere o nome da cidade de nascimento.
# O programa não pode aceitar respostas com menos de 3 caracteres. Force a digitação
# inicial usando a estrutura while True.

while True:
    city_name = input("city name: ")
    if(len(city_name) < 3):
        continue
    else:
        break