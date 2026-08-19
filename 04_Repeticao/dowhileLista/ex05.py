# 5.Escreva um código que receba uma senha do usuário. Se a senha for "senha123",
# imprima "Acesso liberado". Se falhar, exiba a mensagem "Senha incorreta, tente outra
# vez" e reinicie o pedido imediatamente usando o modelo de loop while True.

pin = "senha123"
while True:
    user_password = input("Input your password: ")
    if(user_password == pin):
        print("Acesso liberado")
        break
    else:
        print("Senha incorreta")