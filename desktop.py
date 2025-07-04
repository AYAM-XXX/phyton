import random
import string



def monkey_text_infinite():
    target = "methinks it is like a weasel"  # 28 caracteres
    characters = string.ascii_letters + string.digits + " "  # Inclui espaço
    iterations = 0

    while True:
        string_aleatoria = ''.join(random.choices(characters, k=28))
        iterations += 1
        if string_aleatoria == target:
            print(f"Encontrado: {string_aleatoria}")
            print(f"Iterações necessárias: {iterations}")
            break
        if iterations % 100000000000 == 0:  # Feedback para evitar travamento
            print(f"Iteração {iterations}: {string_aleatoria}")


monkey_text_infinite()
