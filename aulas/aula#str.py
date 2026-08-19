'''aula para teste do curso #'''
# dedicado para os uso do curso
# 0  1 2 3  4  5  6  7 8 9 10 11 12 13 14 15
# e  u   g  o  s  t  o   d  e   m  a  ç  a
texto = '''eu gosto de maça
gosto de feijão'''
email = "AYAM@gmail.com"
esp = "frase"
num = 20000
num2 = round(2.8)

print(texto[3:7])
print(len(texto))
print(email.capitalize())  # deixa a primeira letra maiuscula e o resto min
print(email.casefold())  # deixa tudo minusculo
print(email.count("A"))  # conta quntos character tem
print(email.endswith("gmail.com"))  # verifica se tem tal informação
print(email.find('A'))  # procura o character
print(email.replace('A', 'a'))  # troca um letra por outra
print(email.split('@'))  # separa o texto de uma letra pela outra
print(texto.splitlines())  # separa o texto por character
print(esp.strip(' '))  # tira character do começo e final
print(f'luco foi de {num:,.2f}')  # coloca  o . para separ os numeros
print(num2)  # arredonta o numero
print(f"lucro foi de {num2:.2%}")
