# essa função serve para validar inputs numerico è
# reduzir o uso de condicionais
def validador_num(msg: str, tipo_de_dado: int | float) -> int | float:
    while True:
        try:  # verifica se o usuario colocou um numero certo
            valor = input(msg)
            if tipo_de_dado(valor) > 0:  # verifica se o numero  e negativo

                # faz o casting com o tipo de dado necessario
                return tipo_de_dado(valor)
            else:
                print('valor incorreto')
        except ValueError:
            # caso o valor for uma string ou qualquer entrada invalida
            print('insira novamente o valor :/')
