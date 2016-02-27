"""Verify if the AmericanDate class instantiates and displays properly."""
import view_user_birthdate

def test_americandate():
    """Assert the correct return value for a AmericanDate object when
    its display_date method is called.
    """
    assert view_user_birthdate.AmericanDate('1', '25', '1984').display_date() == '1/25/1984'
