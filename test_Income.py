import pytest

from Income import calculate_income

@pytest.mark.parametrize('summ, rate, period, expected', [
    (700000, 8, 12, 758100)
])

def test_Income(summ, rate, period, expected):
    actual = calculate_income(summ, rate, period)
    assert expected == actual