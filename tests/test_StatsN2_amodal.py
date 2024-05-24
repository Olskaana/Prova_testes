from stat_funcs import StatsN2
import pytest

def test_StatsN2_amodal():
    result = StatsN2.amodal([8, 9])
    assert result == "Não existe moda"


def test_nao_amodal():
    result = StatsN2.amodal([8, 9, 9])
    assert result == "Existe moda"


@pytest.mark.parametrize("numeros, resultado_esperado", [
    ([8,9], "Não existe moda"),
    ([8,9,9], "Existe moda"),
    ([1,4,7,8,9,9], "Existe moda")
])

def test_amodal_esperado(numeros, resultado_esperado):
    result = StatsN2.amodal(numeros)
    assert result == resultado_esperado

@pytest.mark.xfail
def test_amodal_fail():
    resultado = StatsN2.amodal(8,9,10)
    assert resultado == "Existe moda"
