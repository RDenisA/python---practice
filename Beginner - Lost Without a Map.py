#  Given an array of integers, return a new array with each value doubled.
#  For example:
#  [1, 2, 3] --> [2, 4, 6]

def maps(a):
    return [number * 2 for number in a]


print(maps([1, 2, 3]))
