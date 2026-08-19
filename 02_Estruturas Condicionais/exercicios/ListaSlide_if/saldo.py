saldo = float(input("digite o saldo da conta: "))
compra = float(input("digite o valor da compra: "))

if(saldo < compra):
    print("Saldo insuficiente para esta transação!")
else:
    print("compra concluida")



# Crie um script que receba o saldo de uma conta bancária e o valor de uma compra. Se o valor da compra for
# maior que o saldo, exiba a mensagem: "Saldo insuficiente para esta transação!".
