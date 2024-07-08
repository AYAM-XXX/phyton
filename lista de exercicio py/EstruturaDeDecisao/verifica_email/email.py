'''verifica email'''
# verifica se o email está certo
email = input("digite o email: ")
if email:
    if 'gmail' in email and '@' not in email or '.com' not in email:
        print("email invalido do tipo gmail")
    elif ('marto' in email) and ('@' not in email or '.com' not in email):
        print("email invalido do tipo marto")
    else:
        pass

else:
    print("prencha corretamente")
