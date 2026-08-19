ano = int(input(""))
if((ano % 4 == 0 and  ano % 100 != 0) or (ano % 400 == 0)):
    print("bissexto")
else:
    print("ano normal")





# Crie um validador para saber se um ano digitado pelo usuário possui 365 ou 366 dias (Dica: cheque se
# ele é divisível por 4 para descobrir se é bissexto).
# 8 - 1 -1 -1