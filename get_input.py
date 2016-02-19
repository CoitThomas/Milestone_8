"""Get raw input from a user and return it as a string."""

def get_input():
    """Prompt the user for input. Receive the input as raw_input."""
    try:
        return raw_input()
    except EOFError:
        return ' '
