"""Verify if the function format() from class ChineseDate correctly
formats its attributes when called upon.
"""
import view_user_birthdate

def test_chinesedate_format():
    """Assert the correct return value for function format() from
    class ChineseDate.
    """
    assert view_user_birthdate.ChineseDate('1', '25', '1984').format() == '1984/1/25'
