
from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(2003, 5, 17) == "Eleven million, three hundred fifteen thousand, five hundred twenty minutes"
    assert convert_to_minutes(2000, 2, 1) == "Thirteen million, forty-four thousand, nine hundred sixty minutes"
    assert convert_to_minutes(1991, 1, 1) == "Seventeen million, eight hundred twenty-two thousand, eight hundred eighty minutes"
    assert convert_to_minutes(29, 1, 2983) == "Invalid Date"