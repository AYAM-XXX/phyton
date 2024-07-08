'''informe a data'''
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida


def eh_data_valida(data):
    try:
        # Tenta converter a string para uma data
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        # Se houver um erro na conversão, a data é inválida
        return False


# Solicita a data ao usuário
data_input = input("Digite uma data no formato dd/mm/aaaa: ")

# Verifica se a data é válida
if eh_data_valida(data_input):
    print(f"{data_input} é uma data válida.")
else:
    print(f"{data_input} não é uma data válida.")
