"""Verify if the ChineseDate class instantiates and displays properly."""
import view_user_birthdate

def test_chinesedate():
    """Assert the correct return value for a ChineseDate object when
    its display_date method is called.
    """
    assert view_user_birthdate.ChineseDate('1', '25', '1984').display_date() == '1984/1/25'
