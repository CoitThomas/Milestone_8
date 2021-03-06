"""Verify if the function chunk_data() correctly groups lines of data
by 'size' number of lines.
"""
import view_user_birthdate

def test_chunk_data():
    """Assert the correct item in a list is returned when the function
    chunk_data() is called.
    """

    data = """I am the very model of a modern Major-General,
I've information vegetable, animal, and mineral,
I know the kings of England, and I quote the fights historical
From Marathon to Waterloo, in order categorical;"""

    line1 = "I am the very model of a modern Major-General,"
    line2 = "I've information vegetable, animal, and mineral,"
    line3 = "I know the kings of England, and I quote the fights historical"
    line4 = "From Marathon to Waterloo, in order categorical;"

    # Check lower boundary.
    assert view_user_birthdate.chunk_data(data, 1)[0] == [line1]
    # Check the middle.
    assert view_user_birthdate.chunk_data(data, 2)[0] == [line1, line2]
    # Check upper boundary.
    assert view_user_birthdate.chunk_data(data, 4)[0] == [line1, line2, line3, line4]
