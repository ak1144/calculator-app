import pytest
from app import (
    add,
    subtract,
    multiply,
    divide,
    calculate_simple_interest,
    calculate_compound_interest,
)

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5.0
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

def test_calculate_simple_interest():
    # Principal=1000, rate=5%, time=2 years -> Interest = (1000 * 5 * 2)/100 = 100.0
    assert calculate_simple_interest(1000, 5, 2) == 100.0

def test_calculate_compound_interest():
    # Principal=1000, rate=5%, time=2 years, n=1 -> Amount = 1000 * (1.05)^2 = 1102.5, Interest = 102.5
    assert pytest.approx(calculate_compound_interest(1000, 5, 2, 1), 0.01) == 102.5
    # Compounding quarterly n=4
    assert pytest.approx(calculate_compound_interest(1000, 5, 2, 4), 0.01) == 104.49

def test_compound_interest_invalid_n():
    with pytest.raises(ValueError, match="Compounding frequency n must be greater than zero."):
        calculate_compound_interest(1000, 5, 2, 0)
