# 7. Crie um programa que peça uma senha e continue solicitando até que a senha
# correta seja digitada.
password = "abacate"

enterpswd = input("Enter password: ")
while password != enterpswd:
    enterpswd = input("Enter password: ")

print("password acepted")