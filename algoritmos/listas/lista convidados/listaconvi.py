# 3.4 Lista de convidados: Se pudesse convidar qualquer pessoa, viva ou
# falecida, para um jantar, quem você convidaria? Crie uma lista que
# tenha pelo menos três pessoas que gostaria de convidar para um jantar.
# Em seguida, use sua lista a fim de exibir uma mensagem para cada
# pessoa, convidando-a para o jantar.
lista_convidados = ['isadora', 'bistecone', 'jacket']
print(f"{lista_convidados[0].title()}, te convido para um jantar saboroso !!!")
print(f"{lista_convidados[1].title()}, te convido para uma pizza !!!")
print(f"{lista_convidados[2].title()}, te convido para um dogao e dps caçar ums russo !!!")
indisponivel = lista_convidados.pop(2)
print(f"{indisponivel.title()}, foi preso não ira comparecer :/")
lista_convidados.append('renan play')
print(f"{lista_convidados[2].title()}, te convido para um pastel !!!")
lista_convidados.insert(0,'pedro')
lista_convidados.insert(2,'MH')
lista_convidados.insert(3,'biel')
print(f"{lista_convidados[0].title()}, {lista_convidados[2].title()} e {lista_convidados[3].title()} te convido para um churras na minha casa achei uma mesa maior !!!")
print(lista_convidados)
indisponivel = lista_convidados.pop()
print(f"{indisponivel.title()}, a mesa quebrou tenho que desmarcar o compromisso")
indisponivel = lista_convidados.pop()
print(f"{indisponivel.title()}, a mesa quebrou tenho que desmarcar o compromisso")
indisponivel = lista_convidados.pop()
print(f"{indisponivel.title()}, a mesa quebrou tenho que desmarcar o compromisso")
indisponivel = lista_convidados.pop()
print(f"{lista_convidados[0].title()} e {lista_convidados[1].title()}  te convido para um churras na minha casa ainda  tem espaço para vcs 2")
print("nuemro convidado: ", len(lista_convidados))