"""Verify if the Date class instantiates and shows itself properly."""
import view_user_birthdate

def test_date():
    """Assert the correct return value for a Date object when its
    display_date method is called.
    """
    assert view_user_birthdate.Date('1', '25', '1984').show_self() == ('1', '25', '1984')
