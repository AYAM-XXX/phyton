# (Banco de Dados): Crie uma lista de códigos numéricos. Peça para o usuário digitar
# um código no teclado. O programa deve procurar na lista: se achar, mostra em qual
# índice ele está; se não achar após varrer tudo, exiba "Código inexistente".
codigos_int = [
    770487, 216739, 126225, 877572, 388389, 356787, 334053, 246316, 872246, 207473,
    809570, 876646, 671858, 191161, 719176, 542417, 133326, 131244, 198246, 329258,
    343962, 629903, 731262, 127824, 688508, 308496, 850800, 781453, 835392, 671412,
    539898, 331148, 571029, 717889, 391704, 948749, 106814, 895667, 944962, 267414,
    832052, 543143, 456778, 391369, 263032, 325772, 900581, 452944, 207175, 197251,
    498382, 201414, 476417, 988662, 460663, 733052, 377370, 946335, 145561, 865179,
    581741, 662275, 230889, 496922, 182627, 678856, 407419, 969693, 759176, 748564,
    479201, 705397, 301629, 838797, 172933, 148050, 793384, 338968, 910620, 403445,
    183667, 996865, 344098, 205907, 498591, 391476, 575435, 766563, 974628, 482554,
    270555, 488162, 472528, 319684, 802729, 379946, 835911, 816751, 779514, 174870
]

codigo = int(input("digite o codigo que deseja: "))
if codigo in codigos_int:
    for x in range(len(codigos_int)):
        if codigos_int[x] == codigo:
            print(f"indice do codigo {codigo} é {x}")
else:
    print("Código inexistente")
