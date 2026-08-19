'''bonus de venda de funcionario'''
# criar um pograma que da um bonus de venda por funcionario
meta = 20000
vendas = int(input("quantas vendas o funcionario teve: "))
if vendas < meta:
    bonus = 0
    print("não bateu a meta")
elif vendas >= (meta * 2):
    bonus = 0.07
    print(f"seu bonus será: {bonus * 100:.1f}%")
else:
    bonus = 0.03
    print(f"seu bonus será: {bonus * 100}%")
