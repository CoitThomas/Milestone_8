"""Verify if the User class instantiates, formats, and prints properly."""
import view_user_birthdate

def test_date():
    """Assert the correct return value for a printed User object."""
    name = 'orangelover1107'
    nation = 'south korean'
    date = '11/7/1983'
    assert view_user_birthdate.User(name,
                                    nation,
                                    date).format_birthdate().show_self() == ('11', '7', '1983')
