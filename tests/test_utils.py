from strutils.utils import str_valid_int

def test_valid_integer():
    assert str_valid_int(123) == True
    assert str_valid_int(123, True) == 123
    assert str_valid_int('123') == True
    assert str_valid_int('123', True) == 123

def test_valid_float():
    assert str_valid_int(12.3) == False
    assert str_valid_int(12.3, True) == 12
    assert str_valid_int('12.3') == False
    assert str_valid_int('12.3', True) == 12

def test_invalid():
    assert str_valid_int(None) == False
    assert str_valid_int(None, True) == 0
    assert str_valid_int("") == False
    assert str_valid_int("abc") == 0
    assert str_valid_int("abc", True) == 0

















# def test_valid_integer():
#     assert str_valid_int("123") == True
#     assert str_valid_int("123", to_int=True) ==123
#     assert str_valid_int(123, to_int=True) ==123

# def test_invalid_integer():
#     assert str_valid_int("abc") == False
#     assert str_valid_int("12.3") == False

# def test_empty_string():
#     assert str_valid_int("") == False

# def test_non_string_input():
#     assert str_valid_int(None) == False
#     assert str_valid_int(123) == True
#     assert str_valid_int(12.9, to_int=True) == 12

# def test_custom():
#     assert str_valid_int(124) == True