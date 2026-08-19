'''nota'''
# Faça um programa para a leitura de duas notas parciais de um
# # aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# Média de Aproveitamento Conceito
#  Entre 9.0 e 10.0 A
#  Entre 7.5 e 9.0 B
#  Entre 6.0 e 7.5 C
#  Entre 4.0 e 6.0 D
#  Entre 4.0 e zero E

n1 = float(input("digite a nota: "))
n2 = float(input("digite a nota: "))
media = (n1 + n2) / 2
if media >= 9 and media <= 10:
    print("conceito: A")
elif media >= 7.5 and media < 9:
    print("conceito: B")
elif media >= 6 and media < 7.4:
    print("conceito: C")
elif media >= 4 and media < 6:
    print("conceito: D")
elif media < 4 and media > 0:
    print("conceito: E")
else:
    print("digitou errado")
