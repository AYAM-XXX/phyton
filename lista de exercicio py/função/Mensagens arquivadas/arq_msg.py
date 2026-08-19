# Mensagens arquivadas: Comece sua tarefa a partir do Exercício 8.10. Chame a
# função send_messages() com uma cópia da lista de mensagens. Após chamar a
# função, exiba ambas as listas para mostrar que a lista original reteve suas
# mensagens.
mensagens = [
    "Oi! Tudo bem? 😊",
    "Só passei pra dizer que lembrei de você.",
    "Cheguei bem, obrigado por se importar!",
    "Já tô com saudade!",
    "Bom dia! Que hoje seja leve. ☀️",
    "Boa noite! Dorme bem. 😴",
    "Tô torcendo por você! 💪",
    "Precisando, é só chamar.",
    "Foi ótimo te ver hoje.",
    "Tô pensando em você agora.",
    "Passando só pra deixar um abraço virtual. 🤗",
    "Amanhã vai ser melhor, confia.",
    "Que saudade do seu sorriso.",
    "Você ilumina meu dia. ✨",
    "Me avisa quando chegar?"
]
sent_messages = []


def send_messages(mensagens, sent_messages):
    while mensagens:
        msg = mensagens.pop()
        print(f"enviando {msg}...")
        sent_messages.append(msg)


send_messages(mensagens[:], sent_messages)
print(f"\n\nlista original: {mensagens}\n\n")
print(f"lista de mensagem enviadas: {sent_messages}")
