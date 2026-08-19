time1, gols1 = map(int, input("informe o nome com quantidade de gols: ").split())
time2, gols2 = map(int, input("informe o nome  com quantidade de gols: ").split())
if(gols1 > gols2):
    print("time vencedor: " + time1)
else:
    print("time vencedor: " + time2)