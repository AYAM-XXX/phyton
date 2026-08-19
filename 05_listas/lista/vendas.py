# (Vendas): Crie uma lista de clientes vips. O primeiro cliente da lista tem prioridade
# absoluta. Escreva um programa que compare o nome do primeiro cliente com o resto
# da lista para verificar e contar se ele foi cadastrado repetidamente por erro do sistema.


lista_de_nomes = [
    "Leonardo Marques", "Gustavo Gomes", "Nicole Teixeira", "Carlos Lopes", "Laura Fernandes", "Lucas Pinto",
    "Manuela Ramos", "Andre Soares", "Diego Carvalho", "Gustavo Costa", "Thiago Ribeiro", "Alexandre Gomes",
    "Daniel Teixeira", "Joao Lopes", "Valentina Mendes", "Bruno Pereira", "Carlos Melo", "Eduardo Castro",
    "Carlos Teixeira", "Luana Ribeiro", "Gustavo Soares", "Carlos Lima", "Luana Cardoso", "Luiza Nascimento",
    "Murilo Almeida", "Arthur Fernandes", "Rodrigo Rodrigues", "Marcelo Mendes", "Theo Nascimento", "Beatriz Borges",
    "Enzo Nunes", "Beatriz Dias", "Bruno Borges", "Alice Coelho", "Thiago Nascimento", "Bianca Gomes",
    "Enzo Ramos", "Felipe Freitas", "Arthur Moreira", "Heloisa Mendes", "Bruno Martins", "Julia Coelho",
    "Heloisa Fernandes"]

if lista_de_nomes[0] in lista_de_nomes[1:]:
    print("nome cadastrado mais de uma vez")
else:
    print("correto")