# 8. Faça um programa que leia vários números. A entrada deve parar quando o
# usuário digitar 0. Ao final, informe a soma de todos os números digitados
# (exceto o zero)

lista = []
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    else:
        lista.append(num)
        continue
print(lista)