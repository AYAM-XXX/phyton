# Enviando mensagens: Comece com uma cópia do seu programa do Exercício 8.9.
# Escreva uma função chamada send_messages() para exibir cada mensagem de texto
# e passe cada mensagem para uma nova lista chamada sent_messages à medida que
# é exibida. Após chamar a função, exiba ambas as listas para ter certeza de
#  que as mensagens foram corretamente transferidas.
# mensagem de texto.
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


send_messages(mensagens, sent_messages)
print(f"lista original: {mensagens}\n\n")
print(f"lista de mensagem enviadas: {sent_messages}")
