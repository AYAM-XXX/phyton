# 4.10 Fatias: Use um dos programas que escreveu neste capítulo, adicione 
# diversas linhas ao final
# do programa para executarem o seguinte:
# • Exiba a mensagem: Os três primeiros elementos da lista são:. Em seguida,
#  use uma fatia para
# exibir os três primeiros elementos da lista desse programa.
# • Exiba a mensagem: O três elementos que ficam no meio da lista são:.
#  Depois, use uma fatia
# para exibir os três elementos do meio da lista.
# • Exiba a mensagem: Os três últimos elementos da lista são: Em seguida,
#  utilize uma fatia para
# exibir os três últimos elementos da lista.

comidas = ["Pizza", "Sushi", "Lasanha", "Hambúrguer", "Tacos", "Feijoada", "Cuscuz", "Churrasco", "Salada"]

print(f"os tres primeiros elementos da lista são: {comidas[0:3]}")
print(f"os tres elementos do meio da lista são: {comidas[3:6]}")
print(f"os tres elementos do meio da lista são: {comidas[6:]}")
