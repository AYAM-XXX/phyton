# Usuários: Crie uma classe chamada User. Crie dois atributos chamados
# first_name e last_name e diversos outros atributos que normalmente são
# armazenados em um perfil de usuário. Crie um método chamado
# describe_user() que exiba um resumo das informações do usuário. Crie
# outro método chamado greet_user() que exiba um cumprimento
# personalizado ao usuário.
# Crie diversas instâncias que representem usuários distintos e chame
# ambos os métodos para cada um.

# Tentativas de login: Adicione um atributo chamado login_attempts à sua
# classe User do Exercício 9.3 (página 209). Crie um método chamado
# increment_login_attempts() que incrementa o valor de login_attempts em 1.
# Crie outro método chamado reset_login_attempts() que redefine o valor de
# login_attempts para 0.
# Crie uma instância da classe User e chame increment_login_attempts()
# diversas vezes. Exiba o valor de login_attempts para verificar que foi
# incrementado corretamente e, em seguida, chame reset_login_attempts().
# Exiba login_attempts novamente a fim de ter certeza de que foi redefinido
# para 0.


class user:
    def __init__(self, first_name, last_name, age, color_hair):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.color_hair = color_hair
        self.login_attempts = 0

    def describe_user(self):
        print(f"nome completo: {self.first_name} {self.last_name}")
        print(f"idade: {self.age}")
        print(f"cor do cabelo: {self.color_hair}")

    def greet_user(self):
        print(f"\nolá {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


isadora = user('isadora', 'sla', 17, 'azul e preto')
isadora.describe_user()
isadora.greet_user()
print(f"numero de logins: {isadora.login_attempts}")
isadora.increment_login_attempts()
print(f"numero de logins: {isadora.login_attempts}")
isadora.increment_login_attempts()
print(f"numero de logins: {isadora.login_attempts}")
isadora.increment_login_attempts()
print(f"numero de logins: {isadora.login_attempts}")
isadora.reset_login_attempts()
print(f"numero de logins: {isadora.login_attempts}")
