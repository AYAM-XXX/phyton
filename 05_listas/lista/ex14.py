# 14. (E-commerce): Uma lista de preços de produtos contém [100, 200, 300,
# 400]. O site entrou em promoção. Use um laço de repetição para atualizar cada gaveta
# da própria lista, aplicando um desconto de 10% sobre cada valor.

precos = [100, 200, 300, 400]

for x in range(len(precos)):
    precos[x] = precos[x] * 0.90


print(precos)