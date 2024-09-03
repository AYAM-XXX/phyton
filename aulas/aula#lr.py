'''aula de laços de repeteição'''
produtos = ['livro', 'caneta', 'borracha', 'papel']
quantidade = [1000, 1200, 4000, 2000]
for i in range(4):  # for normal
    print(f'produto: {produtos[i]}\nquantidade: {quantidade[i]}\n')
#
for item in produtos:  # for each percorre dentro da lista com um indice espesifico
    print(f'o produto é {item}')
#
for num in quantidade: # for com if: utiliza essas condições para procuras situações mais espesificas
    if num >= 1500:
        print("quantidade boa")
    else:
        print("precisa pedir mais")
for i, item in enumerate(produtos):
    if quantidade[i] <= 1500:
        print(f'precisa comprar mais {item}\n quantidade restante: {quantidade[i]}\n')
