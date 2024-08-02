'''perguntas sobre um crime'''
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
cont = 0
print("Telefonou para a vítima?:\nsim\nnão")
esc = input("digite: ")
if esc == "sim":
    cont += 1
print("Esteve no local do crime?\nsim\nnão")
esc = input("digite: ")
if esc == "sim":
    cont += 1
print("Mora perto da vítima?\nsim\nnão")
esc = input("digite: ")
if esc == "sim":
    cont += 1
print("Devia para a vítima?\nsim\nnão")
esc = input("digite: ")
if esc == "sim":
    cont += 1
print("á trabalhou com a vítima?\nsim\nnão")
esc = input("digite: ")
if esc == "sim":
    cont += 1
if cont <= 2:
    print("suspeita")
elif cont > 3 and cont <= 4:
    print("cumplice")
elif cont == 5:
    print("assasino")
else:
    print("inocente")
