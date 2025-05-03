# Mensagens: Crie uma lista com uma série de mensagens curtas de texto.
# Passe a lista para uma função chamada show_messages(), que exiba cada
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


def show_menssages(mensagens):
    for mensagem in mensagens:
        print(f"{mensagem}")


show_menssages(mensagens)
