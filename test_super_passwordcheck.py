import pytest
from passwordcheck import Passwordcheck

test_data = [
    ("123456789",False), 
    ("abcd1234@",False), 
    ("ABCD1234@",False), 
    ("abCD1234",False), 
    ("Abcd123 @",False), 
    ("        ",False),
    ("AbCD1234@", True),
    ("ABCDASDF", True)
    ]
@pytest.mark.parametrize("password, expected", test_data) 
def test_acceptable_pass(password,expected):
    assert Passwordcheck.is_acceptable_password(password) == expected



