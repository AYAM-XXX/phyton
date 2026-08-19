'''inversor de variaveis'''
# ler 2 valores A e B e apresentar eles que o valor
# A <-- B e B <-- A
varA = int(input("valor de A: "))
varb = int(input("valor de B: "))
print(varA, varb)
varA, varb = varb, varA
print(varA, varb)
# usei o metado atribução multipla
print(varA + varb)
print(varA * varb)
print(float(varA) / float(varb))
print(varA - varb)
print(varA**2)
print(varb**2)
