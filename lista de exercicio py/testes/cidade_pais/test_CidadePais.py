from CidadePais import CidadePais


def test_CidadePais():
    itumbiara = CidadePais('itumbiara', 'brazil', 100_000)
    assert itumbiara == 'Itumbiara, Brazil - 100000'
