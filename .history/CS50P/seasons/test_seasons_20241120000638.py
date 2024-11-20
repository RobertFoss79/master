from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(2003, 5, 17) == "Ten million, three hundred and seventeen thousand, six hundred minutes"

    assert convert_to_minutes(1991, 1, 1) == "Sixteen million, eight hundred and twenty-four thousand, nine hundred and sixty minutes"
    assert convert_to_minutes(29, 1, 2983) == "Invalid Date"