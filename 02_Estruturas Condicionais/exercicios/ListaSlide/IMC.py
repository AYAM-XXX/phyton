peso = int(input("insira o peso: "))
altura = float(input("insira a altura: "))
imc = peso/(altura * altura)
if(imc < 18.5):
    print("Abaixo do peso")
elif (imc > 18.5 and imc <= 24.9):
    print("Peso ideal")
else:
    print("Sobrepeso")



 # peso/(altura x altura)


# Cálculo de IMC Real: Peça o peso e a altura do usuário, calcule o IMC e use elif para classificar: Abaixo de
# 18.5 "Abaixo do peso", até 24.9 "Peso ideal", 25 ou mais "Sobrepeso".