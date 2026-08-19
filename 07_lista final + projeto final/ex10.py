nomes = []
for x in range(0, 8):
    nome = input("insira o nome: ")
    nomes.append(nome)
print(nomes)
nomes.reverse()
print(nomes)
ultimo_item = nomes[-1]
print(f"Ultimo numero da lista: {ultimo_item}")
