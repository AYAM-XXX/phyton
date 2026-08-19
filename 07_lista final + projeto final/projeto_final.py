from statistics import quantiles


def menu():
    print("1- cadastrar livro\n"
          "2- Listar Livros\n"
          "3- Procurar livro pelo titulo\n"
          "4- Alternar quantidade disponivel\n"
          "5- Excluir Livro\n"
          "6- Relatório")

def mostrar_livros(dic):
    print(f"\nautor: {dic["autor"]}\ntitulo: {dic["titulo"]}\nano: {dic["ano"]}" 
          f"\ncodigo: {dic["codigo"]}\ncategoria: {dic["categoria"]}\nquantidade: {dic["quantidade"]}\n")


livros = [
        {
            "codigo": 1,
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "ano": 1899,
            "categoria": "Historia",
            "quantidade": 5
        },
        {
            "codigo": 2,
            "titulo": "O Hobbit",
            "autor": "J.R.R. Tolkien",
            "ano": 1937,
            "categoria": "Aventura",
            "quantidade": 3
        },
        {
            "codigo": 3,
            "titulo": "1984",
            "autor": "George Orwell",
            "ano": 1949,
            "categoria": "Tecnologia",
            "quantidade": 4
        },
        {
            "codigo": 4,
            "titulo": "Orgulho e Preconceito",
            "autor": "Jane Austen",
            "ano": 1813,
            "categoria": "Romance",
            "quantidade": 2
        }
    ]

categorias = (
        "Romance",
        "Aventura",
        "Tecnologia",
        "Historia",
        "Ciência",
        "Infantil"
    )
while True:
    menu()
    escolha = int(input("insira o numero: "))
    match(escolha):
        case 0:
            False
        case 1:
            livro = {}
            titulo = input("insira o titulo: ")
            codigo = int(input("insira o codigo: "))
            while codigo < 0:
                codigo = int(input("insira o codigo manior que 0: "))
            autor = input("insira o autor: ")
            ano = int(input("insira o ano: "))
            print("1- Romance\n2- Aventura\n3- Tecnologia\n4- Historia\n5- Ciência\n6- Infantil")
            escolher_categoria = int(input("escolha sua categoria: "))
            while escolher_categoria < 1 or escolher_categoria > 6:
                print("1- Romance\n2- Aventura\n3- Tecnologia\n4- Historia\n5- Ciência\n6- Infantil")
                escolher_categoria = int(input("escolha sua categoria corretamente: "))
            categoria  = ""
            if escolher_categoria == 1:
                categoria = "Romance"
            elif escolher_categoria == 2:
                categoria = "Aventura"
            elif escolher_categoria == 3:
                categoria = "Tecnologia"
            elif escolher_categoria == 4:
                categoria = "Historia"
            elif escolher_categoria == 5:
                categoria = "Ciência"
            else:
                categoria = "Infantil"

            quantidade = int(input("insira a quantidade: "))
            while quantidade < 0:
                quantidade = int(input("insira a quantidade: "))

            livro["codigo"], livro["titulo"], livro["autor"], livro["ano"], livro["categoria"], livro["quantidade"] = codigo, titulo, autor, ano, categoria, quantidade
            livros.append(livro)


        case 2:
            for livro in livros:
                print("\n")
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}")
            print("\n")

        case 3:
            titulo = input("\ndigite o nome do livro que queira procurar: ")
            for livro in livros:
                if livro["titulo"] == titulo:
                    print(f"\nautor: {livro["autor"]}\ntitulo: {livro["titulo"]}\nano: {livro["ano"]}"
                          f"\ncodigo: {livro["codigo"]}\ncategoria: {livro["categoria"]}\nquantidade: {livro["quantidade"]}\n")

        case 4:
            titulo = input("\ndigite o nome do livro que queira alter quantidade: ")
            quantidade = int(input("insira a quantidade: "))
            for livro in livros:
                if livro["titulo"] == titulo:
                    livro["quantidade"] = quantidade

        case 5:
            codigo = int(input("\ndigite o codigo do livro que queira excluir: "))
            if livro["codigo"] == codigo:
                    livros.remove(livro)
        case 6:

            print(f"Quantidade total de livros: {len(livros)}\n")


            mais_antigo = min(livros, key=lambda livro: livro["ano"])
            print("Livro mais antigo:")
            mostrar_livros(mais_antigo)

            mais_novo = max(livros, key=lambda livro: livro["ano"])
            print("Livro mais novo:")
            mostrar_livros(mais_novo)

            maior_qtd = max(livros, key=lambda livro: livro["quantidade"])
            print("Livro com maior quantidade:")
            mostrar_livros(maior_qtd)


            count = 0
            rmc, avt, tec, hist, cie, infa = 0, 0, 0, 0, 0, 0

            for livro in livros:
                if livro["categoria"] == "Romance":
                    rmc += 1
                elif livro["categoria"] == "Aventura":
                    avt += 1
                elif livro["categoria"] == "Tecnologia":
                    tec += 1
                elif livro["categoria"] == "Historia":
                    hist += 1
                elif livro["categoria"] == "Ciência":
                    cie += 1
                elif livro["categoria"] == "Infantil":
                    infa += 1
                count += 1

            print("Quantidade de livros por categoria:")
            print(f"  Romance: {rmc}")
            print(f"  Aventura: {avt}")
            print(f"  Tecnologia: {tec}")
            print(f"  História: {hist}")
            print(f"  Ciência: {cie}")
            print(f"  Infantil: {infa}\n")

            print(f"Média de livros por categoria: {count / 6:.2f}")


