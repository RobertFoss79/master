import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_hello_case_insensitive():
    assert value("Hello") == 0

def test_value_h():
    assert value("house") == 20

def test_value_h_case_insensitive():
    assert value("House") == 20

def test_value_other():
    assert value("What's up?") == 100
