# Uma instituição de ensino técnico concederá bolsas de estudos para estudantes com
# bom desempenho acadêmico. Para participar do processo seletivo, o candidato deverá
# atender simultaneamente aos seguintes critérios:
# • média final maior ou igual a 8,0;
# • frequência mínima de 75%.
# O setor de Tecnologia da Informação foi responsável por desenvolver um programa
# para auxiliar a comissão avaliadora.
# Desenvolva um algoritmo que solicite:
# • nome do candidato;
# • média final;
# • frequência (%).
# Ao final, informe se o candidato foi classificado ou não classificado, justificando o
# motivo da decisão.


name = input("Enter name: ")
grade_rate = float(input("Enter grade rate: "))
frequency = int(input("Enter frequency of absences: "))
if(grade_rate >= 8 and frequency > 75):
    print("Approved")
else:
    print("Failed")