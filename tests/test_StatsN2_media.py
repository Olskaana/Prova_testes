from stat_funcs import StatsN2
import pytest

def test_StatsN2_media():
    result = StatsN2.media([8, 9])
    assert result == 8,5

def test_media_sem_lista():
    result = StatsN2.media(None)
    assert result == 0

@pytest.mark.parametrize("numeros, result_esperado", [
    ([4, 2], 3),
    ([10, 20, 30], 20)
])

def test_media_esperado(numeros, result_esperado):
    result = StatsN2.media(numeros)
    assert result == result_esperado

@pytest.mark.xfail
def test_media_fail():
    result = StatsN2.media([4, 2])
    assert result == 2