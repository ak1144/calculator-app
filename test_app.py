from app import add, subtract

def test_add():
    assert add(100, 50) == 150
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    assert subtract(100, 50) == 50
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0
    assert subtract(5.5, 2.5) == 3.0
