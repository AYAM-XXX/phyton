# 1. (Pet Shop): O pet shop "Cão Amigo" quer listar seus primeiros clientes do dia. Crie
# uma lista com 5 nomes de cães e imprima em linhas separadas o primeiro e o último
# nome da lista usando índices.

cachorros = ["cupim", "paçoca", "marmita", "rodolfo", "capim"]

for x, cachorro in enumerate(cachorros):
    print(f"{x} - {cachorro}")