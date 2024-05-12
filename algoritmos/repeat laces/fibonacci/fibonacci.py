"""escrever a sequencia de fibonacci"""
# escrever a sequencia de fibonacci ate o 15
# entrada: cont
cont = 0
seq = [0, 1]
while cont <= 15:
    seq = seq[cont] + seq[cont + 1]
    cont = cont + 1
    print(seq)
# não resolvido
