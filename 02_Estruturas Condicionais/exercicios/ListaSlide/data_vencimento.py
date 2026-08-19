data = int(input("insira a data: "))
data_vencimento = int(input("insira a data de vencimento: "))

if(data > data_vencimento):
    print("Boleto Vencido! Juros de atraso aplicados.")
else:
    print("Boleto em dia. Pode pagar normalmente.")












# Validador de Data de Vencimento: Receba o dia atual e o dia de vencimento de um boleto. Se o dia atual
# for maior que o vencimento, exiba "Boleto Vencido! Juros de atraso aplicados.", caso contrário "Boleto em
# dia. Pode pagar normalmente.".
