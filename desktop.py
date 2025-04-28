prompt = "me diga qualquer coisa: "
flag = True
while True:
    mensagem = input(prompt)
    if mensagem == 'sair':
        break
    if mensagem == 'pão':
        continue
    print(mensagem)
