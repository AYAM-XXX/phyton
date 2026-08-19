from collections import deque


def busca_vendedor(grafo, inicio):
    fila_da_pesquisa = deque()
    fila_da_pesquisa += grafo[inicio]
    verificados = set()  # Para evitar loops infinitos

    while fila_da_pesquisa:
        pessoa = fila_da_pesquisa.popleft()
        if pessoa not in verificados:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            # Adiciona os vizinhos à fila
            fila_da_pesquisa += grafo.get(pessoa, [])
            verificados.add(pessoa)

    return False  # Se ninguém for encontrado


# Exemplo de uso:
grafo = {
    'ayam': ['bob', 'claire', 'alice'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}


def pessoa_e_vendedor(nome):
    # Exemplo: considera vendedores nomes terminando em 'm'
    return nome[-1] == 'm'


busca_vendedor(grafo, 'ayam')
