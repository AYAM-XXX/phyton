# Cidade, país: Crie uma função que aceite dois parâmetros: um nome de cidade
# e um nome de país. A função deve retornar uma única string com o formato
# Cidade, País, como Santiago, Chile. Armazene a função em um módulo chamado
# city_functions.py e salve esse arquivo em uma pasta nova para que o pytest
# não tente executar os testes que já escrevemos.

# População: Altere sua função para que exija um terceiro parâmetro,
# population. Agora, a função deve retornar uma única string no formato
# Cidade, País – população xxx, como Santiago, Chile – population 5000000.
#
# Execute o teste mais uma vez e garanta que test_city_country() falhe
# desta vez.
#
# Modifique a função para que o parâmetro population seja opcional. Execute
# o teste e garanta que test_city_country() passe mais uma vez.
#
# Escreva um segundo teste chamado test_city_country_population() que
# verifique se você pode chamar sua função com os valores 'santiago',
# 'chile' e population=5000000. Execute os testes mais uma vez e garanta
# que esse teste novo passe.


def CidadePais(cidade: str, pais: str, population: int) -> str:
    return f"{cidade.title()}, {pais.title()} - {population}"


uberlandia = CidadePais('uberlandia', 'Brazil', 300_000)
print(uberlandia)
