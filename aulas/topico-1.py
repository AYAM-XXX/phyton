#variaveis
a = 1
b = "e maneiro" 
w = "  ayam e brabo  "
c = w+b # junta as variaveis
z = 1+2j
print(w.strip()) # tira os  espaços da beirada da string ex : " amor " passa a ficar "amor"
print(c)
print(w.upper()) # deixa as letras tudo em maiusculas
print(w.lower()) # deixa tudo em minuscula
print("a variavel e do tipo ",type(z)) # informa o tipo de dado
# como transformar uma varivel de qualquer tipo para outro tipo
i = 1
g = "123"
j = 2.9
print(str(i) + str(i))# int(a) muda a varivel a para int .casting concerte o tipo de var
''' variveis tem que ser declaradas com nomes e descrição do tipo de dados 
que elas representa. ex: "a = 32"  varivel a pode significar varias coisas
se for idade seria melhor representar assim idade = 21, seria mais facil
de comprender

variaveis globais = fora de uma funçao sempre fica no pc
variavris locais = sempre existem dentro dessa função '''