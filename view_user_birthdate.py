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
    def __init__(self, username, nationality, birthdate):
        """Instantiate an object with the attributes 'username',
        'nationality', and 'birthdate'. If user is not in the
        bday_book, add the User's username and birthdate.
        """
        assert re.search(r"[\w.-]+", username), "Invalid username."
        assert re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality), "Invalid nationality."
        assert re.search("[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,4}", birthdate), "Invalid birthdate."
        self.username = username.lower()
        self.nationality = nationality.lower()
        self.birthdate = Date(birthdate)

    date_format_by_nationality = {
        'american': AmericanDate,
        'belizean': AmericanDate,
        'micronesian': AmericanDate,
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

    def print_user_birthdate(self):
        assert self.nationality in date_format_by_nationality, "Nationality unknown."
        print date_format_by_nationality[self.nationality](self.birthdate).format_date()

class Date(object):
    """Take in a string in the format:
    mm/dd/yyyy
    Create a Date object from that string with the attributes month,
    day, and year.
    """
    regex_rule = ("(?P<month>[0-9]{1,2})" # Month.
                  "/(?P<day>[0-9]{1,2})" # Day.
                  "/(?P<year>[0-9]{4})" # Year.
                 )

    def __init__(self, string):
        """Instantiate a Date object with the attributes 'month',
        'day', and 'year'.
        """
        assert re.search(Date.regex_rule, string), "A string in the format: mm/dd/yyyy must be provided."
        self.month, self.day, self.year = self.parse_date(string)

    def parse_date(self, string):
        """Take in a string containing a date in the format mm/dd/yyyy and
        return three strings representing a valid day, month, and year.
        """
        date = re.search(Date.regex_rule, string)
        assert date, "A string in the format mm/dd/yyyy must be provided."

        month = self.make_int(date.group('month'))
        day = self.make_int(date.group('day'))
        year = self.make_int(date.group('year'))

        assert self.is_valid_date(month, day, year), "A valid date must be provided."

        return str(month), str(day), str(year)

    def make_int(self, string):
        """Convert a given string to an integer. If it cannot be converted,
        return None.
        """
        try:
            return int(string)
        except ValueError:
            return None

    def is_valid_date(self, month, day, year):
        """Take in three integers representing a month, day, and year.
        Verify they are valid representations and return True or False.
        """
        return self.valid_month(month) and self.valid_day(day, month) and self.valid_year(year)

    def valid_month(self, month):
        """Take in an integer representing a month of the year. Return True
        if it is valid. Otherwise, return False.
        """
        return 1 <= month <= 12

    def valid_day(self, day, month):
        """Take in an integer representing a day and month of the year.
        Return True if it is a valid day for the given month. Otherwise,
        return False.
        """
        month31 = [1, 3, 5, 7, 8, 10, 12]
        month30 = [4, 6, 9, 11]
        assert self.valid_month(month)
        if month in month31:
            return 1 <= day <= 31
        if month in month30:
            return 1 <= day <= 30
        if month == 2:
            return 1 <= day <= 28

    def valid_year(self, year):
        """Take in an integer representing a pertinent year. Return True if
        it is valid. Otherwise, return False.
        """
        return 1800 <= year <= 2200

    def print_date(self):
        print "Month = %s" % self.month
        print "Day = %s" % self.day
        print "Year = %s" % self.year

class AmericanDate(Date):
    """Create an object of type AmericanDate wich inherits from class
    Date.
    """
    def format_date(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the American format:
        mm/dd/yyyy
        """
        return '%s/%s/%s' % (self.month, self.day, self.year)

class EuropeanDate(Date):
    """Create an object of type EuropeanDate which inherits from class
    Date.
    """
    def format_date(self):
        """Using the attributes 'month', 'day', and 'year', return a
        string in the European format:
        dd/mm/yyyy
        """
        return '%s/%s/%s' % (self.day, self.month, self.year)

class ChineseDate(Date):
    """Create an object of type ChineseDate wich inherits from class
    Date.
    """
    def format_date(self):
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
            month, day, year = build_date(birthdate)
            birthdate = format_date(month, day, year, nationality)
            bday_book[username] = User(username, nationality, birthdate)
    return bday_book

if __name__ == "__main__":
    FILE = 'user_data.txt' # Enter filename here.
    BDAY_BOOK = build_bday_book(FILE)
    INPUT = get_input().lower()
    while not INPUT.isspace() and INPUT:
        if INPUT in BDAY_BOOK:
            BDAY_BOOK.print_user_birthdate(INPUT)
        else:
            print "Sorry, user not found."
        INPUT = get_input().lower()
