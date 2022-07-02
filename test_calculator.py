from calculator import Calculator
import pytest

def test_four_is_even():
    assert Calculator.is_even(4)

def test_five_is_odd():
    assert Calculator.is_even(5) == False

def test_fivedotone_isnot_interger():
    # to verify Exception
    with pytest.raises(Exception):
        Calculator.is_even(5.1)
