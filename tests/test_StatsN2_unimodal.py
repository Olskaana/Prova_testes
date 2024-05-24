from stat_funcs import StatsN2
import pytest

def test_StatsN2_unimodal():
    result = StatsN2.unimodal([1,2,3,4,5,5])
    assert result == 5

def test_nao_unimodal():
    result = StatsN2.unimodal(['4, 2, 2, 9, 10, 9'])
    assert result == "Não é unimodal"

@pytest.mark.parametrize("lista, esperado", [
    ([4, 2, 2, 9, 10], 2),
    ([4, 2, 2, 9, 10, 9], "Não é unimodal")
])
def test_unimodal_esperado(lista, esperado):
    result = StatsN2.unimodal(lista)
    assert result == esperado

@pytest.mark.xfail
def test_unimodal_sem_lista_fail():
    result = StatsN2.unimodal(None)
    assert result == "Não é unimodal"