"""Verify if the function build_bday_book() correctly assembles a
dictionary of usernames as the keys and corresponding birthdates as the
values.
"""
import view_user_birthdate

def test_build_bday_book():
    """Assert correct contents of an assmbled bday_book."""
    file_name = 'testfile4build_bday_book.txt'
    bday_book = view_user_birthdate.build_bday_book(file_name)
    # Check entry value types.
    for entry in bday_book:
        assert isinstance(bday_book[entry], view_user_birthdate.User)
    # Check entry filter.
    assert 'austinwiltshire' in bday_book
    assert 'coit125' in bday_book
    assert 'nigelhiggenbothem' in bday_book
    assert 'chenxiang' in bday_book
    assert '' not in bday_book
    assert 'homersimpson' not in bday_book
    assert 'margesimpson' not in bday_book
    count = 0
    for entry in bday_book:
        if entry == 'coit125':
            count = count + 1
    assert count == 1
    # Check a sample entry's values.
    assert bday_book['chenxiang'].get_username() == 'chenxiang'
    assert bday_book['chenxiang'].get_nationality() == 'chinese'
    assert bday_book['chenxiang'].get_birthdate().display_date() == '2/14/1989'
