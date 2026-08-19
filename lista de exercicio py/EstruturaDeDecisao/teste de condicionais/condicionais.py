# Testes condicionais: Escreva uma série de testes condicionais.
#  Exiba uma afirmação com
# cada teste descrito e a previsão dos resultados de cada teste.
#  Seu código deve ficar mais ou
# menos assim:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Preste bastante atenção aos seus resultados e procure entender por
#  que cada linha é avaliada
# como True ou False.
# • Crie, pelo menos, 10 testes. Execute, pelo menos, 5 testes avaliados
#  como True e outros
# 5 testes avaliados como False.

minha_garagem = ['ferrari', 'lamborghini', 'porsche', 'mclaren', 'bugatti',
                 'aston martin', 'corvette', 'mustang', 'camaro', 'nissan gtr']

if 's10' not in minha_garagem:
    print("não tenho")

if 'ferrari' in minha_garagem:
    print(f"tenho")
