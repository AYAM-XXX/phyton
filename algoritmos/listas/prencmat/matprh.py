'''prenche uma matriz'''
# prenche uma matriz com numeros

coluna = []
col = int(input("digite o numero de colunas: "))
lin = int(input("digite o numero de linhas: "))
for i in range(col):
    linha = []
    for j in range(lin):
        linha.append(float(input(f' [{i + 1}][{j + 1}]: ')))
    coluna.append(linha)
print(coluna)
