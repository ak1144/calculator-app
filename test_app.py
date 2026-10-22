import app


def test_add():
    assert app.add(100, 50) == 150
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0
    assert app.add(2.5, 3.5) == 6.0
