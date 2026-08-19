'''criar um verificador de cpf'''
cpf = []
dv = []
for x in range(11):
    cpf.append(int(input("insira um numero: ")))
    if x < 9:
        dv.append(cpf[x])
print(dv)
soma = 0
for x in range(9):
    soma += dv[x] * (10 - x)
dv1 = 11 - (soma % 11)
dv.append(dv1)
soma = 0
for x in range(10):
    soma += dv[x] * (11 - x)
if soma % 11 < 2:
    dv2 = 0
else:
    dv2 = 11 - (soma % 11)
dv.append(dv2)
if cpf == dv:
    print("cpf valido")
else:
    print("cpf invavalido")
