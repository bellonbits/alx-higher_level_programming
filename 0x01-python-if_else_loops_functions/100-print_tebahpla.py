#!/usr/bin/python3

# For ascii_code in range sequence
for ascii_code in range(122, 96, -1):

    # If ascii_code is odd
    if ascii_code % 2 == 1:

        # Convert letter to uppercase
        ascii_code = ascii_code - 32

    # Print out letters
    print("{:c}".format(ascii_code), end="")
