def decompor_numero(numero):
    if numero >= 1000 or numero < 0:
        return "Número fora do intervalo permitido. Deve ser entre 0 e 999."

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")

    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    if not partes:
        return "0 unidades"

    return " e ".join(partes)


# Testando a função com os números fornecidos
testes = [326, 300, 100, 320, 310, 305, 301,
          101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
for numero in testes:
    print(f"{numero} = {decompor_numero(numero)}")
