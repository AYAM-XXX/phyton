estados_nordeste = (
    "Alagoas",
    "Bahia",
    "Ceará",
    "Maranhão",
    "Paraíba",
    "Pernambuco",
    "Piauí",
    "Rio Grande do Norte",
    "Sergipe"
)
estado = input("digite o nome de um estado do nordeste: ")
estado = estado.capitalize()

if estado in estados_nordeste:
    print("Essa estado existe na tupla")
    print(estados_nordeste.index(estado))
else:
    print("Esse estado não existe na tupla")