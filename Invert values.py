#  Given a set of numbers, return the additive inverse of each.
#  Each positive becomes negatives, and the negatives become positives.
#  invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
def invert(lst):
    return [x * -1 for x in lst]


print(invert([1, -2, 3, -4, 5]))
