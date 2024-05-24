from stat_funcs import StatsN2
import pytest

def test_StatsN2_variancia():
    result = StatsN2.variancia([1,2,3,4,4,5,5,6,6])
    assert result == 3.0

@pytest.mark.parametrize("numeros, resultado_esperado", [
    ([4, 2, 9, 10], 10.8125),
    ([1, 2, 3, 4], 1.25),
    ([10, 20, 30, 40], 150.0)
])
def test_variancia_esperado(numeros, resultado_esperado):
    result = StatsN2.variancia(numeros)
    assert result == resultado_esperado

@pytest.mark.xfail
def test_variancia_fail():
    result = StatsN2.variancia(4, 2, 9, 10)
    assert result == 5
