# Álbum:
# Escreva uma função chamada make_album() que crie um dicionário
# representando um álbum de música. A função deve receber o nome de um
# artista e o título do álbum, e retornar um dicionário com essas duas
# informações.
#
# Utilize a função para criar três dicionários representando álbuns distintos.
# Exiba cada valor de retorno para mostrar que os dicionários estão armazenando
# adequadamente as informações do álbum.
#
# Use None para adicionar um parâmetro opcional à função make_album() que
# possibilite armazenar o número de músicas em um álbum. Se a chamada incluir
# um valor para o número de músicas, adicione esse valor ao dicionário doálbum.
#
# Crie pelo menos uma chamada da função que inclua o número de músicas em um
# álbum.
#
# Álbuns de usuários:
# Comece com seu programa do Exercício 8.7. Escreva um loop while que
# possibilite aos usuários inserir o artista e o título de um álbum.
# Após receber essas informações, chame make_album() com a entrada do
# usuário e exiba o dicionário criado.
# Não se esqueça de incluir um valor de saída no loop while.


def make_album(artista, album, num_musicas=None):
    artistas = {'artista': artista,
                'álbum': album}
    if num_musicas:
        artistas['numero de musicas'] = num_musicas
    return artistas


prompt_nome = 'escreva o nome do artista: '
prompt_album = 'escreva o nome do album'
prompt_num_msc = 'escreva o numero de msc'

while True:
    artista = input(prompt_nome)
    if artista == 'sair':
        break
    album = input(prompt_album)
    if album == 'sair':
        break
    num_msc = input(prompt_num_msc)
    if num_msc == 'sair':
        break
    print(make_album(artista, album, num_msc))
