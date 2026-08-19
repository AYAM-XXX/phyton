# Reservas em restaurante: Crie um programa que pergunte quantos lugares
# em uma mesa o
# usuário precisa. Se a resposta for mais de oito, exiba uma mensagem
# informando que é
# necessário aguardar por uma mesa. Caso contrário, informe que a mesa
# já está disponível.

prompt = "quantos lugares de mesa o usuario precisa?"
reserva = input(prompt)
reserva = int(reserva)
if reserva > 0 and reserva < 12:
    if reserva > 8:
        print("aguarde por uma mesa....")
    else:
        print("sua mesa está disponivel")
else:
    print("")
