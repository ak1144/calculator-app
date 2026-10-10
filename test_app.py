import pytest
import app

def test_add():
    assert app.add(10, 5) == 15
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0
    assert app.add(1.5, 2.5) == 4.0

def test_subtract():
    assert app.subtract(10, 5) == 5
    assert app.subtract(5, 10) == -5
    assert app.subtract(0, 0) == 0
    assert app.subtract(5.5, 2.5) == 3.0
