from checkpass import Check_password
# Test case: Password without special letter.
def test_password_without_special():
    password = 'DuyVo0123'
    assert Check_password.check_password(password) == False