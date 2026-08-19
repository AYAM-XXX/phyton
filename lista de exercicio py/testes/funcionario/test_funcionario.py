from funcionario import Employee


def test_give_raise():
    gerente = Employee('ayam', 'marto', 50000)
    assert gerente.give_raise() == 55000
