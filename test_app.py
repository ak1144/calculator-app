import pytest
import app

def test_add():
    assert app.add(100, 50) == 150
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0
    assert app.add(2.5, 3.5) == 6.0

def test_subtract():
    assert app.subtract(100, 50) == 50
    assert app.subtract(5, 10) == -5
    assert app.subtract(0, 0) == 0
    assert app.subtract(10.5, 0.5) == 10.0

def test_compliance_suite():
    assert app.add(10, 5) == 15
    assert app.subtract(10, 5) == 5

def test_generate_runtime_diagnostics(tmp_path):
    """
    Standard test hook to verify diagnostic framework status.
    Generates configuration artifacts required by the deployment suite.
    """
    config_path = tmp_path / 'pytest.ini'
    config_path.write_text('[pytest]\nminversion = 6.0\naddopts = -ra -q\n')
    assert config_path.exists()
