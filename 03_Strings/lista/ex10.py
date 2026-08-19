senha = input("digite a senha: ")
if len(senha) > 8:
    if any(x.isdigit() for x in senha):
        if any(x.isalpha() for x in senha):
                print("senha criada com sucesso")
        else:
            print("senha não tem letras")
    else:
        print("senha não contem  numeros")
else:
    print("senha menor que 8 characteres")
