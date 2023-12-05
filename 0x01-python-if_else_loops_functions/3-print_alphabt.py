#!/usr/bin/python3

# For each ascii_code in range sequence
for ascii_code in range(97, 123):

    # If ascii_code match code for 'q' and 'e' skip it
    if ascii_code == 101 or ascii_code == 113:
        continue

    # Print out the character format of the ascii_code
    print("{:c}".format(ascii_code), end='')
