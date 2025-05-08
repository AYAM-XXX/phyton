def inserir(nota: list[float]) -> list[float]:
    while True:
        entrada = input("insira a nota: ")
        if entrada.lower() == 'sair':
            return nota
        else:
            try:
                nota_aluno = float(entrada)
                if (nota_aluno > 0) and (nota_aluno <= 10):
                    nota.append(nota_aluno)
                else:
                    print(f"\nrepita denovo {nota_aluno} é invalido\n")
            except ValueError:
                print("\ntipo invalido de entrada\n")
