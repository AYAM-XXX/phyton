'''verifica p tamamho de strings'''
# Faça um programa que leia 2 strings e informe o conteúdo
# delas seguido do seu comprimento. Informe também se as duas strings possuem o
# mesmo comprimento e são iguais ou diferentes no conteúdo
texto_1 = 'Brasil Hexa 2006'
texto_2 = 'Brasil Hexa 2006'
# tamamho
if len(texto_1) == len(texto_2):
    print("tem o mesmo tamanho")
    print(f"tamanho texto 1: {len(texto_1)}")
    print(f"tamanho texto 2: {len(texto_2)}")
else:
    print("tem tamanho diferentes")
    print(f"tamanho texto 1: {len(texto_1)}")
    print(f"tamanho texto 2: {len(texto_2)}")
if texto_1 == texto_2:
    print("são iguais de conteudo")
else:
    print("são diferentes de conteudo")
