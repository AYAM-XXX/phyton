'''elevar um numero a potencia de 3'''
# ler um numero qualquer menor ou igual a 50 e apresentar o valor
# obtido da multiplicaçãp sucessiva de N por 3 enquanto o produto for menor
# que 250 (N*3; N*3*3;N*3*3*3)
# entrada: int(nmr)
# saida: int(produto)
nmr = int(input("digite um numero: "))
produto = 0
cont = 1
while nmr < 0 or nmr > 50:
    nmr = int(input("digite um numero menor ou igual a 50 e maior que 0: "))
produto = nmr
while produto < 250:
    print(produto)
    produto = nmr * (3**cont)
    cont = cont + 1
