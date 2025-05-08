from inserir_notas import inserir_nota
from cad_aluno import cadastrar
from media import media_nota as exibir_media
from relatorio import exibir_notas
alunos = {}


def menu():
    print("\n1 - Cadastrar aluno")
    print("2 - Inserir nota")
    print("3 - Calcular média")
    print("4 - Ver relatório")
    print("5 - Sair")


while True:
    menu()
    escolha = input("escolha um numero: ")
    match escolha:
        case '1':
            nome = input("digite o nome do aluno: ").lower()
            cadastrar(alunos, nome)
        case '2':
            nota = []
            nome = input("digite o nome do aluno: ").lower()
            inserir_nota(alunos, nome, nota)
        case '3':
            nome = input("digite o nome do aluno: ").lower()
            exibir_media(alunos, nome)
        case '4':
            exibir_notas(alunos)
        case '5':
            break
        case _:
            print("\n\ntente novamente\n\n")
