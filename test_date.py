"""Verify if the Date class instantiates and displays properly."""
import view_user_birthdate

def test_date():
    """Assert the correct return value for a Date object when its
    display_date method is called.
    """
    assert view_user_birthdate.Date('1/25/1984').display_date() == '1/25/1984'
