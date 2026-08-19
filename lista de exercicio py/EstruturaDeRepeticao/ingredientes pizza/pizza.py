# Ingredientes de pizza: Escreva um loop que solicite ao usuário uma série
# de ingredientes de
# pizza até que ele forneça o valor 'quit'. À medida que cada ingrediente
# é fornecido, exiba uma
# mensagem informando que esses ingredientes estão sendo adicionados à pizza.
prompt = "digite o ingrediente que quer colocar: "
ingrediente = ''
active = True
while active:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        active = False
    else:
        print(f"colocando {ingrediente} na pizza")
