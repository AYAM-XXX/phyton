# Sanduíches: Crie uma função que aceite uma lista de itens que uma pessoa
# deseja em um sanduíche. A função deve ter um parâmetro que colete todos os
# itens fornecidos na chamada da função e deve exibir um resumo do sanduíche
# que está sendo solicitado. Chame a função três vezes, com um número
# diferente de argumentos a cada vez.

def make_sandwich(*ingredientes):
    print("ingredientes solicitados: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


make_sandwich('alface', 'tomate', 'frango', 'maionese', 'mussarela')