dinheiro = float(input("insira o valor:"))
print(" digite \n1-Dólar\n2-Euro\n3-Libra")
escolha = int(input("insira o numero: "))
if(escolha == 1):
    print("Voce escolheu dolar")
    dolar = 5
    print(f"conversão de dolar para reais: {(dolar * dinheiro):.2f}")
    print(f"conversão de reais para dolar: {(dinheiro / dolar):.2f}")
elif(escolha == 2):
    print("Voce escolheu euro")
    euro = 5.82
    print(f"conversão de euro para reais: {(euro * dinheiro):.2f}")
    print(f"conversão de reais para euro: {(dinheiro / euro):.2f}")
elif (escolha == 3):
    print("Voce escolheu libra")
    libra = 6.79
    print(f"conversão de libra para reais: {(libra * dinheiro):.2f}")
    print(f"conversão de reais para libras: {(dinheiro / libra):.2f}")
else:
    print("valor incorreto")




# Conversor de Moedas Dinâmico: Crie um menu onde o usuário escolhe a moeda de destino para converter
# $R\$\,100.00$: 1-Dólar, 2-Euro, 3-Libra. Faça o cálculo e imprima o valor convertido usando a estrutura
# estudada