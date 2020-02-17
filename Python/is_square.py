# is an integer square?

import math

def is_square(n):
    # positive integers only
    if n < 0:
        return False
    # math.sqrt returns a float, and squaring this value may not be accurate
    # int() takes the floor of a number, and adding 0.5 to it should mean
    # that we get the value we are looking for if the float is close enough
    # to the int we need
    root = math.sqrt(n)
    return n == int(root + 0.5) ** 2

print(is_square(4))
print(is_square(7))
print(is_square(1000373))