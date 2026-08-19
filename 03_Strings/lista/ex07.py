arquivo = input("insira o nome do arquivo: ")
arquivo = arquivo.split(".")
primeira_parte = arquivo[0]
segunda_parte = arquivo[1]
inversor = segunda_parte + "." +  primeira_parte[::-1]
print(inversor)