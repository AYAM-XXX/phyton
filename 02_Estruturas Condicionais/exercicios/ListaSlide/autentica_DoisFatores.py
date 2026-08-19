
senha_input = input("")
senha = "12345"
twofa = "123"
if(senha_input == senha):
    print("SENHA CORRETA")
    twofa_input = input("insira os 2 fatores: ")
    if(twofa_input == twofa):
        print("2FA CORRETO!")
    else:
        print("2FA INCORRETO!")
else:
    print("SENHA INCORRETA")







