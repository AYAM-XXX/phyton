aluno = {
    "nome" : "Kaio",
    "nota" : 8.8,
    "endereço": {
        "rua": "Rua dos ovo",
        "numero" : 14,
        "bairro" : "Tulipa"
    }

}
for chave, valor in aluno.items():
    if isinstance(valor, dict):
        for chave2, valor2 in valor.items():
            print(f"{chave2} : {valor2}")
    else:
        print(f"{chave} : {valor}")