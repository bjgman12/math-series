from math_series import __version__
from math_series.series import fib
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    actual = fib(1)
    expected = 0
    assert actual == expected

def test_five():
    actual = fib(5)
    expected = 3
    assert actual == expected


# Lucas Testing

def test_lucas_one():
    actual = lucas(1)
    expected = 2
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected =  7
    assert actual == expected

# Series Test

def test_sum_series_one_param():
    actual = sum_series(6)
    expected = 5
    assert actual == expected

def test_sum_series_lucas_param():
    actual = sum_series(6,2,1)
    expected = 11
    assert actual == expected