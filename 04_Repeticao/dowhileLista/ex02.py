# 2.Escreva um programa que simule a digitação de um PIN de segurança bancária de 4
# dígitos. O loop executa pedindo o PIN. Se o PIN digitado for correto ("2026"), o loop
# quebra. Caso contrário, informa o erro e pede novamente.

pin = "2026"
while True:
    user_password = input("Input your password: ")
    if(user_password == pin):
        print("Password approved :)")
        break