from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(1979, 6, 4) == "Twenty-three million, nine hundred and eleven thousand, two hundred minutes"
    assert convert_to_minutes(2015, 3, 18) == "Five million, eighty-eight thousand, nine hundred and sixty minutes"
    assert convert_to_minutes(1975, 11, 25) == "Twenty-five million, seven hundred and sixty-four thousand, four hundred and eighty minutes"
    assert convert_to_minutes(29, 1, 2983) == "Invalid Date"