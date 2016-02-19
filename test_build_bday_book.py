"""Verify if the function build_bday_book() correctly assembles a
dictionary of usernames as the keys and corresponding birthdates as the
values.
"""
import view_user_birthdate

def test_build_bday_book():
    """Assert correct contents of an assmbled bday_book."""
    file_name = 'testfile4build_bday_book.txt'
    assert view_user_birthdate.build_bday_book(file_name) == {'austinwiltshire':'4/20/1983',
                                                              'nigelhiggenbothem':'19/9/1985',
                                                              'coit125':'1/25/1984',
                                                              'chenxiang':'1989/2/14'}
