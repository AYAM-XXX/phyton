# Dicionário do usuário: o exemplo remember_me.py armazena apenas uma
# informação, o nome de usuário. Incremente esse exemplo solicitando mais
# duas informações sobre o usuário e armazene todas as informações
# coletadas em um dicionário. Escreva esse dicionário em um arquivo com
# json.dumps(), e o releia usando json.loads(). Exiba um resumo mostrando
# exatamente o que seu programa relembra sobre o usuário.

from pathlib import Path
import json

path = Path(
    'lista de exercicio py/json/Dicionário_do_usuário/usuario.json')

users = {}


def armazenar(conteudo):
    try:
        path.write_text(json.dumps(conteudo))  # escreve no arquivo json
    except FileNotFoundError:
        print("arquivo não encontrado")


def inputs_usuarios(usuarios):
    nome = input("digite o nome do usuario: ")
    idade = input("digite a idade do usuario: ")
    cor_cabelo = input("digite a cor do cabelo do usuario: ")
    usuarios['nick'] = nome
    usuarios['idade'] = idade
    usuarios['cor do cabelo'] = cor_cabelo


def ler_info(arquivo):
    if arquivo.exists():
        user = arquivo.read_text(encoding='utf-8')
        ler_user = json.loads(user)
        print(ler_user)
    else:
        print("não existe nada")


inputs_usuarios(users)
armazenar(users)
ler_info(path)
