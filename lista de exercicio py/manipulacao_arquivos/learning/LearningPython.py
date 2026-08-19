# Convidados: Escreva um programa que solicite ao usuário seu nome.
# Quando responder, escreva o nome dele em um arquivo chamado guest.txt.

from pathlib import Path
path = Path('lista de exercicio py/manipulacao_arquivos/learning/frase.txt')

ler_arquivo = path.read_text()
print(ler_arquivo.replace('pastel', 'coxinha'))
