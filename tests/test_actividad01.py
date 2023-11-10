import pytest
from src.ejercicio_2_3_3 import hacerSerie

@pytest.mark.parametrize(
    "input_1, expected",
    [
        (2, "2,1,0"),
        (4, "4,3,2,1,0")
        
    ]
)
def test_hacerSerie_params(input_1, expected):
    assert hacerSerie(input_1) == expected


"""
def test_dividir_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        dividir(1200.456, 0)
"""