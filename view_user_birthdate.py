"""Build a dictionary of usernames and their corresponding birthdates
formatted to match their respective nationalities. Additionally, take
in user input, match it to any usernames in the dictionary and return
that user's formatted birthdate.
"""
import re
from get_input import get_input

REGEX_DATE_RULE = ("(?P<month>[0-9]{1,2})" # Month.
                   "/(?P<day>[0-9]{1,2})" # Day.
                   "/(?P<year>[0-9]{4})" # Year.
                  )

class Date(object):
    """Take in a string in the format:
    mm/dd/yyyy
    Create a Date object from that string with the attributes month,
    day, and year.
    """
    def __init__(self, string):
        """Instantiate a Date object with the attributes 'month',
        'day', and 'year'.
        """
        assert_response = "A string in the format mm/dd/yyyy must be provided."
        assert re.search(REGEX_DATE_RULE, string), assert_response
        self._month, self._day, self._year = parse_date(string)

    def get_date_attributes(self):
        """Return the Date objects month, day, and year."""
        return self._month, self._day, self._year

    def display_date(self):
        """Return a string in the format:
        mm/dd/yyyy
        """
        month, day, year = self.get_date_attributes()
        return "%s/%s/%s" % (month, day, year)

class EuropeanDate(Date):
    """Create an EuropeanDate which will display its date in the format:
    dd/mm/yyyy
    """
    def display_date(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the European format:
        dd/mm/yyyy
        """
        month, day, year = self.get_date_attributes()
        return '%s/%s/%s' % (day, month, year)

class ChineseDate(Date):
    """Create a ChineseDate which will display its date in the format:
    yyyy/mm/dd
    """
    def display_date(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the Chinese format:
        yyyy/mm/dd
        """
        month, day, year = self.get_date_attributes()
        return '%s/%s/%s' % (year, month, day)

class User(object):
    """ Take in two strings 'username' and 'nationality' and a Date
    'birthdate'. Create an object of type User with those same
    variables as attributes. Keep track of all instantiated User
    objects with the dictionary 'bday_book'.
    """
    def __init__(self, username, nationality, birthdate):
        """Instantiate an object with the attributes 'username',
        'nationality', and 'birthdate'. If user is not in the
        bday_book, add the User's username and birthdate.
        """
        assert re.search(r"[\w.-]+", username), "Invalid username."
        assert re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality), "Invalid nationality."
        assert re.search("[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,4}", birthdate), "Invalid birthdate."
        self._username = username.lower()
        self._nationality = nationality.lower()
        self._birthdate = Date(birthdate)

    def get_username(self):
        """Return the User object's username."""
        return self._username

    def get_nationality(self):
        """Return the User object's nationality."""
        return self._nationality

    def get_birthdate(self):
        """Return the User object's username."""
        return self._birthdate

    def print_birthdate(self):
        """Format and print the User's birthdate according to its nationality."""
        print self.format_birthdate().display_date()

    def format_birthdate(self):
        """Format the User's birthdate according to its nationality."""
        date_format_book = {
            'american': Date,
            'belizean': Date,
            'micronesian': Date,
            'british': EuropeanDate,
            'irish': EuropeanDate,
            'german': EuropeanDate,
            'italian': EuropeanDate,
            'spanish': EuropeanDate,
            'australian': EuropeanDate,
            'new zealander': EuropeanDate,
            'south african': EuropeanDate,
            'brazilian': EuropeanDate,
            'mexican': EuropeanDate,
            'indian': EuropeanDate,
            'indonesian': EuropeanDate,
            'nigerian': EuropeanDate,
            'russian': EuropeanDate,
            'canadian': EuropeanDate,
            'french': EuropeanDate,
            'chinese': ChineseDate,
            'north korean': ChineseDate,
            'south korean': ChineseDate,
            'japanese': ChineseDate,
            'taiwanese': ChineseDate,
            'hungarian': ChineseDate,
            'lithuanian': ChineseDate,
            'iranian': ChineseDate
        }
        assert self.get_nationality() in date_format_book, "Nationality format unknown."
        return date_format_book[self.get_nationality()](self.get_birthdate().display_date())

def parse_date(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return three strings representing a valid day, month, and year.
    """
    date = re.search(REGEX_DATE_RULE, string)
    assert date, "A string in the format mm/dd/yyyy must be provided."

    month = make_int(date.group('month'))
    day = make_int(date.group('day'))
    year = make_int(date.group('year'))

    assert is_valid_date(month, day, year), "A valid date must be provided."

    return str(month), str(day), str(year)

def make_int(string):
    """Convert a given string to an integer. If it cannot be converted,
    return None.
    """
    try:
        return int(string)
    except ValueError:
        return None

def is_valid_date(month, day, year):
    """Take in three integers representing a month, day, and year.
    Verify they are valid representations and return True or False.
    """
    return valid_month(month) and valid_day(day, month) and valid_year(year)

def valid_month(month):
    """Take in an integer representing a month of the year. Return True
    if it is valid. Otherwise, return False.
    """
    return 1 <= month <= 12

def valid_day(day, month):
    """Take in an integer representing a day and month of the year.
    Return True if it is a valid day for the given month. Otherwise,
    return False.
    """
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    assert valid_month(month)
    if month in month31:
        return 1 <= day <= 31
    if month in month30:
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= 28

def valid_year(year):
    """Take in an integer representing a pertinent year. Return True if
    it is valid. Otherwise, return False.
    """
    return 1800 <= year <= 2200

def read_file(file_name):
    """Read in data from a file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def chunk_data(file_data, size):
    """Take in data as a string and an integer as a string. Return a
    list containing chunks of data that are 'size' number of lines
    each.
    """
    data_lines = file_data.splitlines()

    assert data_lines, "There is no data!"
    assert int(size), "An integer in the form of a string must be provided."
    assert 0 < int(size) <= len(data_lines), "A valid size must be provided."
    assert len(data_lines) % size == 0, "Data is incomplete."

    return [data_lines[pos:pos + size] for pos in range(0, len(data_lines), size)]

def parse(regex, group_name, data_chunk):
    """Take in a chunk of data. Parse the code according to a given
    regular expression. Group the parsed data according to a given
    group name and return it. If there is not a match, return None.
    """
    # Parse username.
    parsed_data = re.search(regex, data_chunk)
    if parsed_data:
        return parsed_data.group(group_name)
    else:
        return None

def build_bday_book(file_name):
    """Take in the name of a file. Use the contents of the file to
    build a dictionary where the keys of the dictionary are the
    usernames and the values are the corresponding birthdates.
    """
    bday_book = {}
    data = read_file(file_name)
    assert data, "There is no data!"
    data_chunks = chunk_data(data, 3)
    for chunk in data_chunks:
        username = parse(r"username:(?P<username>[\w.-]+)", 'username', chunk[0])
        nationality = parse("nationality:(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)",
                            'nationality', chunk[1])
        birthdate = parse("birthdate:(?P<birthdate>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})",
                          'birthdate', chunk[2])
        if username and nationality and birthdate:
            bday_book[username] = User(username, nationality, birthdate)
    return bday_book

if __name__ == "__main__":
    FILE = 'user_data.txt' # Enter filename here.
    BDAY_BOOK = build_bday_book(FILE)
    USERNAME = get_input().lower()
    while not USERNAME.isspace() and USERNAME:
        if USERNAME in BDAY_BOOK:
            BDAY_BOOK[USERNAME].print_birthdate()
        else:
            print "Sorry, user not found."
        USERNAME = get_input().lower()
