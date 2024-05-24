from stat_funcs import StatsN2
import pytest

def test_StatsN2_media_ponderada():
    num = [1, 2, 3, 4, 5]
    pesos = [1, 2, 3, 4, 5]
    result = StatsN2.media_ponderada(num, pesos)
    assert result == 8.545454545454545

def test_media_ponderada_sem_lista():
    result = StatsN2.media_ponderada(None, None)
    assert result == 0

@pytest.mark.xfail
def test_media_ponderada_fail():
    num = [2, 3, 2, 3]
    pesos = [2, 3, 2, 3]
    result = StatsN2.media_ponderada(num, pesos)
    assert result == 2

@pytest.mark.parametrize("numeros, pesos, result_esperado", [
    ([2, 3, 2, 3], [1, 1, 1, 1], 2),
    ([1, 2, 3], [1, 2, 3], 2.333)
])
def test_media_ponderada_esperada(num, pesos, result_esperado):
    result = StatsN2.media_ponderada(num, pesos)
    assert result == result_esperado
