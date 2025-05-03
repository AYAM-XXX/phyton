# Perfil de usuário: Comece com uma cópia do arquivo user_profile.py da
# página 194. Crie um perfil de si mesmo chamando build_profile(), com seu
# primeiro nome, sobrenome e três outros pares chave-valor que o representem.

def build_profile(nome, sobrenome, **additions):
    additions['sobrenome'] = sobrenome
    additions['nome'] = nome

    return additions


def print_profiles(profiles):
    print("perfil do usuario: ")
    for key, value in reversed(profiles.items()):
        print(f"{key}: {value}")


profile = build_profile('ayam', 'marto', altura=1.85,
                        peso='90kg', genero='masculino')
print_profiles(profile)
