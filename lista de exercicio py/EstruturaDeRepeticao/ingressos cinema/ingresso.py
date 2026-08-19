# Ingressos de cinema: Um cinema cobra preços de ingressos diferentes,
# dependendo da idade
# da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito;
#  se tiver entre 3 e 12 anos, o
# ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso
# custa US$15. Escreva um loop
# que pergunte a idade dos usuários e, em seguida, informe o preço do
# ingresso do cinema.

prompt = "qual a sua idade? "
idade = ''
active = True
while active:
    idade = input(prompt)
    idade = int(idade)
    if idade >= 0 and idade < 3:
        print('valor do ingresso: gratuito')
    elif idade >= 3 and idade <= 12:
        print('valor do ingresso: US$10')
    elif idade > 12:
        print('valor do ingresso: US$15')
    else:
        print('idade não existente')
