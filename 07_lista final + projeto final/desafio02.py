cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte",
           "Brasília", "Salvador", "Fortaleza", "Curitiba",
           "Manaus", "Recife", "Porto Alegre", "Belém", "Goiânia",
           "Guarulhos", "Campinas", "São Luís", "São Gonçalo", "Maceió",
           "Duque de Caxias", "Natal", "Teresina")


cidade = input("insira o nome da cidade: ").capitalize()

if cidade in cidades:
    print("Essa cidade existe na tupla")
    print(f"indice da tupla que se encontra: {cidades.index(cidade)}")
else:
    print("cidade não existe")

print(f"tamanho da tupla: {len(cidades)}")
