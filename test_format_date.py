"""Verify if the function format_date() determines and returns the
correct format of the given month, day, and year based on the given
nationality.
"""
import view_user_birthdate

def test_format_date():
    """Assert the correct values and format order for various inputs
    to format_date().
    """
    # Check American format.
    assert view_user_birthdate.format_date('1', '25', '1984', 'american') == '1/25/1984'
    # Check European format.
    assert view_user_birthdate.format_date('5', '14', '1946', 'italian') == '14/5/1946'
    # Check Chinese format.
    assert view_user_birthdate.format_date('6', '17', '1955', 'japanese') == '1955/6/17'
    # Check missing nationality.
    assert not view_user_birthdate.format_date('1', '23', '1987', 'homerland')
