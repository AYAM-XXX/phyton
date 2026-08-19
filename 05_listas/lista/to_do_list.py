tarefas = []

def menu():
    print("========== GERENCIADOR DE TAREFAS ==========")
    print("1- Adicionar tarefas")
    print("2- Listar tarefas")
    print("3- Remover tarefas")
    print("4- Sair")

def listar_tarefas(tarefas):
    print("\n========== LISTA DE TAREFAS ==========")
    for x, tarefa in enumerate(tarefas):
        print(f"{x + 1}- {tarefa}")
    print("======================================\n")

state_of_loop = True
while state_of_loop:
    menu()
    escolha = int(input("digite: "))

    match escolha:
        case 1:
            print("Digite no final PARAR para poder parar de adicionar tarefas")
            while True:
                add_tarefa = input("digite sua tarefa: ")
                if add_tarefa.upper() == 'PARAR':
                    break
                else:
                    tarefas.append(add_tarefa)
                    continue
        case 2:
            listar_tarefas(tarefas)

        case 3:
            listar_tarefas(tarefas)
            remover_tarefa = int(input("Digite o indice da tarefa que deseja remover: "))
            while remover_tarefa < 1 or remover_tarefa > (len(tarefas)):
                print("Esse indice não existe escreva novamente")
                remover_tarefa = int(input("Digite o indice da tarefa que deseja remover: "))
            tarefas.pop(remover_tarefa - 1)
            print("terefa removida com sucesso!!!!")
            listar_tarefas(tarefas)
        case 4:
            print("Finalizando programa....")
            state_of_loop = False

        case _:
            print("valor digitado errado no menu")







