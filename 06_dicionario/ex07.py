funcionario = {
    "nome": "KAIO",
    "cargo": "Eng de Software",
    "salario" : 10000

}
print(funcionario.get("salario"))
funcionario["salario"] = funcionario.get("salario") * 1.10
print(funcionario.get("salario"))