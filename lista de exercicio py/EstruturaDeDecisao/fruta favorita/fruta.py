# Fruta favorita: Crie uma lista de suas frutas favoritas e,
#  em seguida, escreva uma série de
# declarações if independentes que verificam determinadas
#  frutas em sua lista.
# • Crie uma lista com suas três frutas favoritas e a nomeie
#  como favorite_fruits.
# • Escreva cinco instruções if. Cada uma deve verificar se
#  um determinado tipo de fruta consta
# em sua lista. Se sim, o bloco if deve exibir uma afirmação
#  do tipo: Você realmente gosta de
# bananas!
favorite_fruits = ['jaboticaba', 'banana', 'laranja', 'uva', 'abacaxi',
                   'morango', 'melancia', 'kiwi', 'manga', 'coco']
if 'banana' in favorite_fruits:
    print('voce curte banana em!!!')
if 'morango' in favorite_fruits:
    print('voce curte morango em!!!')
if 'uva' in favorite_fruits:
    print('voce curte uva em!!!')
if 'jaboticaba' in favorite_fruits:
    print('voce curte jaboticaba em!!!')
if 'laranja' in favorite_fruits:
    print('voce curte laranja em!!!')
if 'maçã' not in favorite_fruits:
    print('essa fruta e uma merda em!!!')