# Um milhão: Crie uma lista com números de um a um milhão e, em seguida,
# utilize um loop for para exibi-los. (Se a saída estiver demorando muito
# , interrompa-a pressionando CTRL+C ou fechando a janela de saída.)

lista = [num for num in range(1, 1_000_001)]
for num in lista:
    print(num)

print(min(lista))
print(max(lista))
print(sum(lista))