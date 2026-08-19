'''fundo de investimentos'''
# fundo de investimetos
meta = 0.05
taxa = 0
rendimento = float(input("digite o rendimento: "))
if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f"sera cobrado {taxa * 100}% de taxa")
    else:
        taxa = 0.02
        print(f"sera cobrado {taxa * 100}% de taxa")
else:
    taxa = 0
    print(f"sera cobrado {taxa * 100}% de taxa")
