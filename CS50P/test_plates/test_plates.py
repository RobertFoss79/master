import pytest
from plates import is_valid

def test_valid_plates():
    assert is_valid("RF1234") == True
    assert is_valid("CS50") == True
    assert is_valid("HEYYO") == True
    assert is_valid("R1F2C3") == False
    assert is_valid("REF123") == True
    assert is_valid("ROBERT") == True

def test_starts_with_two_letters():
    assert is_valid("R12345") == False
    assert is_valid("12345R") == False
    assert is_valid("RF1234") == True

def test_invalid_plates_length():
    assert is_valid("R") == False
    assert is_valid("RF12345") == False

def test_invalid_plates_non_alphanumeric():
    assert is_valid("RFC123!") == False
    assert is_valid("RF CD") == False

def test_invalid_plates_starting_number():
    assert is_valid("1RFC23") == False

def test_invalid_plates_number_placement():
    assert is_valid("REF12D") == False
    assert is_valid("RF0C12") == False
    assert is_valid("RF12C") == False

def test_invalid_plates_number_order():
    assert is_valid("RF0123") == False

def test_valid_plates_numbers_in_middle():
    assert is_valid("RF123") == True
    assert is_valid("RF12C") == False
