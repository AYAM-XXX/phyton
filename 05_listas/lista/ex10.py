# (Tarefas): Crie uma lista com 4 tarefas diárias. Utilize um laço while para exibir as
# tarefas enumeradas de 0 a 3 de acordo com seu índice.

tarefas = ["escovar os dentes", "tomar banho", "varrer a casa", "dormir"]
cont = 0
while (cont < len(tarefas)):
    print(f"{cont} {tarefas[cont]}")
    cont += 1