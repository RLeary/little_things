# Returns a list of all ints in a string
# Eg, get_ints_from_string(10, then 23 and finally -13)
# returns [10, 23, -13]

from re import findall

def get_ints_from_string(string):
    return [int(i) for i in re.findall(r'\d+|-\d+', string)]
