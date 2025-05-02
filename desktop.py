designs = ['deafpool', 'M4 competition', 'livro de capas']
final_designs = []


def complete_design(unfinished_designs, finished_designs):
    while unfinished_designs:
        unfinished_design = unfinished_designs.pop()
        print(f"trabalhando com {unfinished_design}")
        finished_designs.append(unfinished_design)


def finished_list(listas):
    print("\n\ndesign prontos: ")
    for item in listas:
        print(f"- {item} está pronto")


complete_design(designs[:], final_designs)
finished_list(final_designs)
print(designs)
