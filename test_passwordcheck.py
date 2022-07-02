from passwordcheck import Passwordcheck

def test_length_password():
    assert Passwordcheck.is_acceptable_password("123456789") == False

def test_uppercase_password():
    assert Passwordcheck.is_acceptable_password("abcd1234@") == False

def test_lowercase_password():
    assert Passwordcheck.is_acceptable_password("ABCD1234@") == False

def test_symbol_password():
    assert Passwordcheck.is_acceptable_password("abCD1234") == False

def test_invalidChar_password():
    assert Passwordcheck.is_acceptable_password("Abcd123 @") == False

def test_valid_password():
    assert Passwordcheck.is_acceptable_password("@bcD1234") == True

def test_valid_password12():
    assert Passwordcheck.is_acceptable_password("        ") == False
