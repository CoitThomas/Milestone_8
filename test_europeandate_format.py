"""Verify if the function format() from class EuropeanDate correctly
formats its attributes when called upon.
"""
import view_user_birthdate

def test_europeandate_format():
    """Assert the correct return value for function format() from
    class EuropeanDate.
    """
    assert view_user_birthdate.EuropeanDate('1', '25', '1984').format() == '25/1/1984'
