"""Build a dictionary of usernames and their corresponding birthdates
formatted to match their respective nationalities. Additionally, take
in user input, match it to any usernames in the dictionary and return
that user's formatted birthdate.
"""
import re
from get_input import get_input

class User(object):
    """ Take in two strings 'username' and 'nationality' and a Date
    'birthdate'. Create an object of type User with those same
    variables as attributes. Keep track of all instantiated User
    objects with the dictionary 'bday_book'.
    """
    bday_book = {}

    def __init__(self, username, nationality, birthdate):
        """Instantiate an object with the attributes 'username',
        'nationality', and 'birthdate'. If user is not in the
        bday_book, add the User's username and birthdate.
        """
        assert re.search(r"[\w.-]+", username), "Invalid username."
        assert re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality), "Invalid nationality."
        assert re.search("[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,4}", birthdate)
        self.username = username.lower()
        self.nationality = nationality.lower()
        self.birthdate = birthdate
        # Add user to the bday_book.
        if self.username not in User.bday_book:
            User.bday_book[username] = self.birthdate

class Date(object):
    """Take in three strings 'month', 'day', and 'year' and create a
    Date object with those same strings as the attributes.
    """
    def __init__(self, month, day, year):
        """Instantiate a Date with the attributes 'month', 'day', and
        'year'.
        """
        assert valid_month(make_int(month)), "Invalid month."
        assert valid_day(make_int(day), make_int(month)), "Invalid day."
        assert valid_year(make_int(year)), "Invalid year."
        self.month = month
        self.day = day
        self.year = year

class AmericanDate(Date):
    """Create an object of type AmericanDate wich inherits from class
    Date.
    """
    nationalities = ['american', 'belizean', 'micronesian']
    def format(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the American format:
        mm/dd/yyyy
        """
        return '%s/%s/%s' % (self.month, self.day, self.year)

class EuropeanDate(Date):
    """Create an object of type EuropeanDate which inherits from class
    Date.
    """
    nationalities = ['british', 'irish', 'german', 'italian',
                     'spanish', 'australian', 'new zealander',
                     'south african', 'brazilian', 'mexican',
                     'indian', 'indonesian', 'nigerian',
                     'russian', 'canadian', 'french'] # Abbreviated list.
    def format(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the European format:
        dd/mm/yyyy
        """
        return '%s/%s/%s' % (self.day, self.month, self.year)

class ChineseDate(Date):
    """Create an object of type ChineseDate wich inherits from class
    Date.
    """
    nationalities = ['chinese', 'north korean', 'south korean',
                     'japanese', 'taiwanese', 'hungarian',
                     'lithuanian', 'iranian'] # Abbreviated list.
    def format(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the Chinese format:
        yyyy/mm/dd
        """
        return '%s/%s/%s' % (self.year, self.month, self.day)

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

def parse(data_chunk):
    """Take in a chunk of data 3 lines long. Parse the 3 lines of code
    into their corresponding parts: username, nationality, and
    birthdate. Then return the parsed parts.
    """
    # Parse username.
    first_line = re.search(r"username:(?P<username>[\w.-]+)", data_chunk[0])
    if first_line:
        username = first_line.group('username')
    else:
        username = None

    # Parse nationality.
    second_line = re.search("nationality:"
                            "(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)", data_chunk[1])
    if second_line:
        nationality = second_line.group('nationality')
    else:
        nationality = None

    # Parse birthdate.
    last_line = re.search("birthdate:"
                          "(?P<birthdate>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", data_chunk[2])
    if last_line:
        birthdate = last_line.group('birthdate')
    else:
        birthdate = None

    return username, nationality, birthdate

def build_bday_book(file_name):
    """Take in the name of a file. Use the contents of the file to
    build a dictionary where the keys of the dictionary are the
    usernames and the values are the corresponding birthdates.
    """
    data = read_file(file_name)
    assert data, "There is no data!"
    data_chunks = chunk_data(data, 3)
    for chunk in data_chunks:
        username, nationality, birthdate = parse(chunk)
        if username and nationality and birthdate:
            month, day, year = build_date(birthdate)
            birthdate = format_date(month, day, year, nationality)
            # Instantiate a User object thus adding the User to the bday_book.
            User(username, nationality, birthdate)
    return User.bday_book

def build_date(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return three strings representing a valid day, month, and year.
    """
    regex_rule = ("(?P<month>[0-9]{1,2})" # Month.
                  "/(?P<day>[0-9]{1,2})" # Day.
                  "/(?P<year>[0-9]{4})" # Year.
                 )
    date = re.search(regex_rule, string)
    assert date, "A string in the format mm/dd/yyyy must be provided."

    month = make_int(date.group('month'))
    day = make_int(date.group('day'))
    year = make_int(date.group('year'))

    if is_valid_date(month, day, year):
        return str(month), str(day), str(year)

def format_date(month, day, year, nationality):
    """Take in four strings 'month', 'day', 'year' and 'nationality'.
    Use the given nationality to determine what type of Date object to
    return. Return None if there is not a nationality match.
    """
    assert valid_month(make_int(month)), "Invalid month."
    assert valid_day(make_int(day), make_int(month)), "Invalid day."
    assert valid_year(make_int(year)), "Invalid year."
    assert re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality), "Invalid nationality."
    if nationality.lower() in AmericanDate.nationalities:
        return AmericanDate(month, day, year).format()
    if nationality.lower() in EuropeanDate.nationalities:
        return EuropeanDate(month, day, year).format()
    if nationality.lower() in ChineseDate.nationalities:
        return ChineseDate(month, day, year).format()
    return None

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

if __name__ == "__main__":
    FILE = 'user_data.txt' # Enter filename here.
    BDAY_BOOK = build_bday_book(FILE)
    INPUT = get_input()
    while not INPUT.isspace() and INPUT:
        if INPUT.lower() in BDAY_BOOK:
            print BDAY_BOOK.get(INPUT.lower())
        else:
            print "Sorry, user not found."
        INPUT = get_input()
