# 8. Tupla de Trás para Frente
# Receba uma frase do usuário, converta as palavras dessa frase em uma tupla e
# exiba os elementos dessa tupla na ordem inversa (do último para o primeiro).


tupla = tuple((map(str,input("digite a palavra: ").split(" "))))
print(tupla)