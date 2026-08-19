'''triangulo'''
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um
# triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for
# maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
ld_1 = int(input("informe o lado: "))
ld_2 = int(input("informe o lado: "))
ld_3 = int(input("informe o lado: "))
if ld_1 == ld_2 and ld_2 == ld_3:
    print("equilatero")
elif ld_1 == ld_2 or ld_2 == ld_3 or ld_1 == ld_3:
    print("isósceles")
else:
    print("escaleno")
