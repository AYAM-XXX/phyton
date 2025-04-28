'''cadastro pessoa'''
# fazer uma matriz que cadastre o : nome, cep, bairro, telefone
# e em seguida mostre esses dados

cad = []
for i in range(2):
    dados = []
    for j in range(5):
        if j == 0:
            dados.append(input("digite o nome:"))
        elif j == 1:
            dados.append(input("digite o endereço:"))
        elif j == 2:
            dados.append(input("digite o cep:"))
        elif j == 3:
            dados.append(input("digite o bairro:"))
        else:
            dados.append(input("digite o telefone:"))
    cad.append(dados)
for i in range(2):
    print("--------//--------")
    print("dados pessoais\n")
    for j in range(5):
        if j == 0:
            print(f"nome: {cad[i][j]}")
        elif j == 1:
            print(f"endereço: {cad[i][j]}")
        elif j == 2:
            print(f"cep: {cad[i][j]}")
        elif j == 3:
            print(f"bairro:{cad[i][j]}")
        else:
            print(f"telefone:{cad[i][j]}")
            print("--------//--------\n")
