from datetime import date
from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(1979, 6, 4, date(2000, 1, 1)) == "Twenty-three million, nine hundred eleven thousand, two hundred minutes"
    assert convert_to_minutes(2015, 3, 18, date(2000, 1, 1)) == "Five million, eighty-eight thousand, nine hundred sixty minutes"
    assert convert_to_minutes(1975, 11, 25, date(2000, 1, 1)) == "Twenty-five million, seven hundred sixty-four thousand, four hundred eighty minutes"

