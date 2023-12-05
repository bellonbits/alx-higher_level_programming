#!/usr/bin/python3

def uppercase(str):
    """Prints uppercase string

    Args:
        str: a character string argument
    """

    # For each letter in str
    for letter in str:

        # Get the letter ascii code
        ascii_letter_code = ord(letter)

        # If the letter is in the lowercase range
        if ascii_letter_code in range(97, 123):

            # Set it to the uppercase value
            ascii_letter_code = ascii_letter_code - 32

        # Print out the uppercase value as character
        print("{:c}".format(ascii_letter_code), end="")
    print()
