# 4. Contador de Ocorrências
# Dada a tupla votos = ('A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'A', 'B'), use as ferramentas de tupla
# para contar quantos votos o candidato 'A' recebeu e exiba o resultado.

votos = ('A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'A', 'B')
cont_A = 0
cont_B = 0
cont_C = 0

for voto in votos:
    if voto == "A":
        cont_A += 1
    elif (voto == "B"):
        cont_B += 1
    else:
        cont_C += 1

print(f"Candidato A recebeu: {cont_A} votos")
print(f"Candidato B recebeu: {cont_B} votos")
print(f"Candidato C recebeu: {cont_C} votos")