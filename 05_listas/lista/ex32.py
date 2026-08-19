# 32.Desafio 2 (Ordenação de Ranking Manual): Uma máquina de fliperama possui uma lista desordenada com 6
# pontuações de jogadores: [520, 1100, 250, 890, 1400, 600]. Escreva um algoritmo usando laços de
# repetição aninhados (um laço dentro do outro) que ordene essa lista do maior para o menor valor, sem usar nenhuma
# função pronta de ordenação do Python. Mostre a lista ordenada.

pontuacao = [520, 1100, 250, 890, 1400, 600]

for x in range(len(pontuacao)):
    for y in range(len(pontuacao) - 1):
        if pontuacao[y] < pontuacao[y + 1]:
            pontuacao[y], pontuacao[y+1] = pontuacao[y+1],pontuacao[y]

print(pontuacao)
