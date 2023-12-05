#!/usr/bin/python3

def remove_char_at(str, n):
    """Removes the char at an index in a given string

    Args:
        str: string argument
        n: index argument

    Returns:
        str: edited string
    """

    # If the index is a positive integer
    if n >= 0:

        # Use slicing to ommit the character at index n
        str = str[:n] + str[n + 1:]

    # Return editied string
    return str
