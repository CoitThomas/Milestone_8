"""Verify if the function parse() correctly extracts and returns a
username, nationality, and birthdate from a list of 3 strings.
"""
import view_user_birthdate

def test_parse():
    """Assert the correct return values for username, nationality, and
    birthdate.
    """
    # Expected input.
    list1 = ['username:orangelover1107', 'nationality:south korean', 'birthdate:11/7/1983']
    assert view_user_birthdate.parse(list1) == ('orangelover1107', 'south korean', '11/7/1983')

    # Check username.
    list1 = ['!@#username:coit125', 'nationality:american', 'birthdate:1/25/1984']
    assert view_user_birthdate.parse(list1) == ('coit125', 'american', '1/25/1984')
    list1 = ['username:coit125!@#', 'nationality:american', 'birthdate:1/25/1984']
    assert view_user_birthdate.parse(list1) == ('coit125', 'american', '1/25/1984')
    list1 = ['1234567', 'nationality:american', 'birthdate:1/25/1984']
    assert view_user_birthdate.parse(list1) == (None, 'american', '1/25/1984')

    # Check nationality.
    list1 = ['username:orangelover1107', '!@#nationality:south korean', 'birthdate:11/7/1983']
    assert view_user_birthdate.parse(list1) == ('orangelover1107', 'south korean', '11/7/1983')
    list1 = ['username:orangelover1107', 'nationality:south korean123', 'birthdate:11/7/1983']
    assert view_user_birthdate.parse(list1) == ('orangelover1107', 'south korean', '11/7/1983')
    list1 = ['username:orangelover1107', 'nationality@south korean', 'birthdate:11/7/1983']
    assert view_user_birthdate.parse(list1) == ('orangelover1107', None, '11/7/1983')

    # Check birthdate.
    list1 = ['username:austinwiltshire', 'nationality:american', '!@#birthdate:4/20/1983']
    assert view_user_birthdate.parse(list1) == ('austinwiltshire', 'american', '4/20/1983')
    list1 = ['username:austinwiltshire', 'nationality:american', 'birthdate:4/20/1983ABC']
    assert view_user_birthdate.parse(list1) == ('austinwiltshire', 'american', '4/20/1983')
    list1 = ['username:austinwiltshire', 'nationality:american', 'birthdate:austinwiltshire']
    assert view_user_birthdate.parse(list1) == ('austinwiltshire', 'american', None)
