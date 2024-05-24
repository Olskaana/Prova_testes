from stat_funcs import StatsN2
import pytest

def test_StatsN2_multimodal():
    result = StatsN2.multimodal([1,2,3,4,4,5,5,6,6])
    assert result == [4, 5, 6]

def test_nao_multimodal():
    result = StatsN2.multimodal(['1,2,3,4,5'])
    assert result == "Não é multimodal"

@pytest.mark.parametrize("numeros, resultado_esperado", [
    (['4, 2, 9, 10'], "Não é multimodal"),
    (['1, 2, 3, 4'], "Não é multimodal")
])

def test_multimodal_esperado(numeros, resultado_esperado):
    result = StatsN2.multimodal(numeros)
    assert result == resultado_esperado

@pytest.mark.xfail
def test_multimodal_fail():
    result = StatsN2.multimodal([4, 2, 2, 9, 9, 10])
    assert result == [2, 9]
