'''vertical em escada'''
# Modifique o programa anterior de forma a mostrar o
# nome em formato de escada
frase = input("digite a frase: ")

for x in range(len(frase)):
    print(frase[:x + 1])