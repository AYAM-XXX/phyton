# Nível Difícil
#
# Exercício 8 (Contextualizado): Um sistema de logs de servidor registra linhas como:
# "2026-05-19 [ERROR] Falha de backup no banco". Escreva um extrator que capture apenas o nível do erro
# (o texto que esteja dentro dos colchetes, neste caso: "ERROR").

msg = "2026-05-19 [ERROR] Falha de backup no banco"
primeira_parte = msg.split("[")[1]
segunda_parte = primeira_parte.split("]")[0]
print(segunda_parte)