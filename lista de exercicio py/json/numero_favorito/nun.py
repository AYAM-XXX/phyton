# Número favorito: Desenvolva um programa que solicite o número favorito do
# usuário.Use json.dumps() para armazenar esse número em um arquivo.
# Escreva um programa separado que leia esse valor e exiba a mensagem:
# “Eu sei o seu número favorito! É _____”.

from pathlib import Path
import json

path = Path(
    'lista de exercicio py/json/numero_favorito/NumFav.json')


def input_number():
    numero = input("digite seu numero favorito: ")
    path.write_text(json.dumps(numero))


def show_number():
    conteudo = path.read_text(encoding='utf-8')
    ler_conteudo = json.loads(conteudo)
    return ler_conteudo


input_number()
numero_fav = show_number()
print(f"numero favorito é: {numero_fav}")
