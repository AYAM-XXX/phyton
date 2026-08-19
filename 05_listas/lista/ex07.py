# (Concessionária): Crie uma lista de carros. Use uma estrutura condicional if
# associada ao tamanho da lista para exibir "Estoque Vazio" se não houver itens, ou
# "Estoque Ativo" caso contrário.

carros = ["fusca", "chevette", "D20", "opala", ""]
if not carros:
    print("Estoque vazio")
else:
    print("Estoque cheio")