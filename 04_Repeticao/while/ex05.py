
# 5.Faça um programa que peça um nome de usuário e uma senha. A senha não pode
# ser igual ao nome do usuário. O sistema deve mostrar uma mensagem de erro e
# continuar pedindo as informações até que os dados sejam criados corretamente.

name = input("Enter name: ")
password = input("Enter password: ")
while password == name:
    password = input("Enter password corretcly: ")

print(f"Name: {name} password: {password}")