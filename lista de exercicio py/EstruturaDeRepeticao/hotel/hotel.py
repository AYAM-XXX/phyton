'''hospedes de quarto de hotel'''
# cria um pograma que faz a lista dos hospedes de um hotel
qtd_pessoas = int(input("quantas pessoas tem no quarto: "))
quarto = []
for i in range(qtd_pessoas):
    nome = input("digite o nome do hospede: ")
    cpf = input("digite o cpf do hospede: ")
    hospede = [nome, 'cpf: ' + cpf]
    quarto.append(hospede)
print(quarto)