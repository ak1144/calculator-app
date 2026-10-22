import os
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


def test_environment_flags(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    assert app.get_environment() == "production"

    monkeypatch.setenv("BUILD_FLAG", "true")
    assert app.is_build_enabled() is True

    monkeypatch.setenv("BUILD_FLAG", "false")
    assert app.is_build_enabled() is False
