import pytest
from twttr import shorten

def test_no_vowels():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("python") == "pythn"

def test_mixed_case_vowels():
    assert shorten("Hello") == "Hll"
    assert shorten("WORLD") == "WRLD"
    assert shorten("PyThOn") == "PyThn"

def test_no_vowel_words():
    assert shorten("rhythm") == "rhythm"
    assert shorten("fly") == "fly"

def test_empty_string():
    assert shorten("") == ""

def test_numbers_and_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("12345") == "12345"
    assert shorten("hello123") == "hll123"

def test_mixed_content():
    assert shorten("Hello, World! 123") == "Hll, Wrld! 123"
