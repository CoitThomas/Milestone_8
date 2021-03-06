"""Verify if the function parse() correctly utilizes a given regex to
parse, group, and return desired information from a string.
"""
import view_user_birthdate

def test_parse():
    """Assert the correct return values when parse is called to parse,
    group and retun desired information from a string.
    """
    regex = "(?P<name>[a-zA-Z]+ ?[a-zA-Z]*)"
    assert view_user_birthdate.parse(regex, 'name', '07734 Hyewon Namkung') == 'Hyewon Namkung'
    assert not view_user_birthdate.parse(regex, 'name', '123450987*&!@#$')
