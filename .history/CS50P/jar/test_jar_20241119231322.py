import pytest
from jar import Jar


def test_init():
    Jar()

def test_str():

    jar = Jar()

    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():

    jar = Jar()

    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(74)

def test_withdraw():

    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(58)