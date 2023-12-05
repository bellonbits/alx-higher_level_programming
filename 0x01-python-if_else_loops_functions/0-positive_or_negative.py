#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Print out the value of number followed by ...
# ..." is positive", if number is greater than zero
if number > 0:
    print("{} is positive".format(number))

# ..." is negative", if number is less than zero
elif number < 0:
    print("{} is negative".format(number))

# ..." is zero", if number is equals to zero
else:
    print("{} is zero".format(number))
