cores = ("Azul", "Verde", "Amarelo", "Vermelho", "Preto")

cor = input("digite o nome de uma cor: ")
cor = cor.capitalize()

if cor in cores:
    print("Essa cor existe na tupla")
else:
    print("Essa cor não existe")