# Camiseta: Crie uma função chamada make_shirt() que aceita um tamanho
# e o texto que deve
# ser estampado na camiseta. A função deve exibir uma frase resumindo
# o tamanho da camiseta e
# a mensagem estampada nela.

def make_shirt(tamanho='G', texto_estampa='eu gosto de python'):
    frase = f"tamanho da camiseta: {tamanho}\nmensagem da estampa: {texto_estampa}"
    return frase


camiseta = make_shirt('P', 'gosto de xereca')
print(camiseta)
camiseta = make_shirt()
print(camiseta)