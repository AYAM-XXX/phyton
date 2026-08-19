# Números ímpares: Use o terceiro argumento da função range() para criar
# uma lista com números ímpares de 1 a 20. Use o loop for para exibir
# cada número
impares = [num for num in range(1, 21,) if num % 2 != 0]
for impar in impares:
    print(impar)