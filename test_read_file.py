"""Verify if the function read_file() correctly reads and returns the
information found in a text file.
"""
import view_user_birthdate

def test_read_file():
    """Assert the correct return value from the function read_file()."""
    assert view_user_birthdate.read_file('testfile4read_file.txt') == """ABCDEFGHIJKLMNOPQRSTUVWXYZ?
abcdefghijklmnopqrstuvwxyz."""
