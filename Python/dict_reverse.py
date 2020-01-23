# Reverse a dict - keys become values and vice versa. Only works  where every 
# value in dict is unique

DICT = {
    'a': '1',
    'b': '2',
    'c': '3'
}

REVERSED_DICT = dict(zip(DICT.values(), DICT.keys()))

print(DICT)
print(REVERSED_DICT)