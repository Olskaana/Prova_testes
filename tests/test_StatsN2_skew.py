from stat_funcs import StatsN2
import pytest

def test_StatsN2_skew():
    result = StatsN2.skew('Distribuição negativa')
    assert result == 'Distribuição negativa'


@pytest.mark.parametrize("lista, esperado", [
    ([4, 3, 5, 7], "Distribuição positiva"),
    ([7, 5, 3, 4], "Distribuição negativa"),
    ([4, 4, 4, 4], "Distribuição normal")
])
def test_skew_esperado(lista, esperado):
    result = StatsN2.skew(lista)
    assert result == esperado


def test_skew_positiva():
    result = StatsN2.skew([4, 3, 5, 7])
    assert result == "Distribuição positiva"


def test_skew_negativa():
    result = StatsN2.skew([7, 5, 3, 4])
    assert result == "Distribuição negativa"


def test_skew_zero():
    result = StatsN2.skew(['4, 4, 4, 4'])
    assert result == "Distribuição normal"


@pytest.mark.xfail
def test_skew_negativa_fail():
    result = StatsN2.skew(['7, 5, 3, 4'])
    assert result == "Distribuição negativa"



