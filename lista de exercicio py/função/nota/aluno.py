# riar um sistema que permite cadastrar alunos, inserir suas notas,
# calcular médias e mostrar relatórios.

# Requisitos:
# Crie as seguintes funções:

# cadastrar_aluno(lista, nome)
# → Adiciona um aluno com nome e uma lista vazia de notas.

# inserir_nota(lista, nome, nota)
# → Adiciona uma nota ao aluno, se ele estiver cadastrado.

# calcular_media(lista, nome)
# → Calcula e mostra a média do aluno.

# relatorio(lista)
# → Exibe todos os alunos com suas notas e médias.
import cad_aluno as cad
import inserir_nota as nota
import calcular_media as media
import relatorio as rel
import veirifica_aluno as vf
alunos_notas = {}

while True:
    print("\n\n1 - Cadastrar aluno")
    print("2 - Inserir nota")
    print("3 - Calcular média")
    print("4 - Ver relatório")
    print("5 - Sair")
    escolha = input("digite um numero: ")
    escolha = int(escolha)

    if escolha == 1:  # cadastro de alunos
        nome_aluno = input("digite o nome do aluno: ")
        cad.cadastrar_aluno(lista=alunos_notas, nome=nome_aluno)

    elif escolha == 2:  # inserir nota
        lista_de_notas = []
        nome_aluno = input("digite o nome do ALUNO: ").strip.lower()
        if vf.verifica(nome_aluno, alunos_notas):
            while True:  # recolhe as nota dos aluno é coloca na lista
                nota_aluno = input("digite a nota do aluno: ")
                if nota_aluno == 'sair':  # para de recolher as notas
                    break
                else:
                    nota_aluno = float(nota_aluno)
                    lista_de_notas.append(nota_aluno)
            nota.inserir_nota(nome_aluno, lista_de_notas, alunos_notas)
        else:
            print("\n\naluno não existente\n\n")

    elif escolha == 3:  # calcula a media dos aluno
        nome_aluno = input("digite o nome do aluno: ")
        media_da_nota = media.calcular_media(nome_aluno, alunos_notas)
        print(f"\naluno: {nome_aluno}\nmedia: {media_da_nota}")

    elif escolha == 4:  # printa o relatorio
        rel.relatorio(alunos_notas)
    else:
        break
