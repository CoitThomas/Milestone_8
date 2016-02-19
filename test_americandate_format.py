"""Verify if the function format() from class AmericanDate correctly
formats its attributes when called upon.
"""
import view_user_birthdate

def test_americandate_format():
    """Assert the correct return value for function format() from
    class AmericanDate.
    """
    assert view_user_birthdate.AmericanDate('1', '25', '1984').format() == '1/25/1984'
