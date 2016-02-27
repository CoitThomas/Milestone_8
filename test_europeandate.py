"""Verify if the EuropeanDate class instantiates and displays properly."""
import view_user_birthdate

def test_europeandate():
    """Assert the correct return value for a EuropeanDate object when
    its display_date method is called.
    """
    assert view_user_birthdate.EuropeanDate('1', '25', '1984').display_date() == '25/1/1984'
