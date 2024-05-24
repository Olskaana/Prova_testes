from stat_funcs import StatsN2
import pytest

def test_StatsN2_dpadrao():
    result = StatsN2.dpadrao(3.0)
    assert result == 1.7320508075688772

@pytest.mark.parametrize("numeros, result_esperado", [
    ([1,2,3,4,4,5,5,6,6], 1.870828693),
    ([10, 20, 30, 40], 12.909944487358056),
    ([2, 4, 6, 8, 10], 3.1622776601683795)
])
def test_dpadrao_esperado(numeros, result_esperado):
    result = StatsN2.dpadrao(StatsN2.variancia(numeros))
    assert result == result_esperado

@pytest.mark.xfail
def test_dpadrao_fail():
    resultado = StatsN2.dpadrao(3.0)
    assert resultado == 2