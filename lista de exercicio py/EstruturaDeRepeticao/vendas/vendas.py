'''meta de vendas'''
# verificar qual funcionario bateu a meta de vendas

meta = 550
vendas = [
    ['maria', 345],
    ['joão', 590],
    ['andreza', 289],
    ['rosangela', 790],
    ['antonio', 590]
]

for item in vendas:
    if item[1] >= meta:
        print(f'funcionario {item[0]} bateu a meta !!!')
    else:
        pass
