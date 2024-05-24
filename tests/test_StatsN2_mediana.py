from stat_funcs import StatsN2
import pytest

def test_StatsN2_mediana():
    result = StatsN2.mediana([1,2,3,4,4,5,5,6,6])
    assert result == 4


def test_mediana_sem_lista():
    result = StatsN2.mediana(None)
    assert result == 0

def test_mediana_resto_diferente_de_0():
    result = StatsN2.mediana([8.8,8.8,8.8,8.8])
    assert result == 8.8

@pytest.mark.parametrize("numeros, resultado_esperado", [
    ([4, 2, 8, 9, 10], 8),
    ([4, 2, 6, 2], 2),
    ([5.5, 5.5, 5.5, 5.5], 5.5)
])

def test_mediana_esperado(numeros, resultado_esperado):
    result = StatsN2.mediana(numeros)
    assert result == resultado_esperado

@pytest.mark.xfail
def test_mediana_fail():
    result = StatsN2.mediana([4, 2, 8, 9, 10])
    assert result == 2