# 3. Buscando no Catálogo
# Crie uma tupla contendo 6 nomes de produtos de um supermercado. Peça para o
# usuário digitar o nome de um produto. Se o produto estiver na tupla, mostre em
# qual posição (índice) ele está. Caso contrário, exiba uma mensagem dizendo que
# o produto não foi encontrado.

tupla = ("queijo", "goiaba", "sal", "arroz", "ratoeira", "qualhada")

busca = input("digite o produto que voce procura: ")

if busca in tupla:
    print(f"O indice da palavra buscada é {tupla.index(busca)}")
else:
    print("item não existe na tupla")
