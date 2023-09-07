from working import convert


def test_valid_1():
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


def test_valid_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
