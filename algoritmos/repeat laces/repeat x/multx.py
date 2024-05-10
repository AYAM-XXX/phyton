''' multiplicar x'''
# fazer um progama que multiplica x por 3 e mostra a resposta
# repetir isso por 5 vezes
# entrada: x, cont = 1
# saida = r

cont = "s"
while cont == "s":
    ent_x = int(input("digite um valor: "))
    print(f'resposta: {ent_x * 3}')
    cont = input("refazer calculo?: s ou n")
