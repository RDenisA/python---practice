import math


def litres(time):
    drink = time * 0.5
    return math.floor(drink)


print(litres(12.3))

# 0.5 литра в час
#  time = 3 ----> litres = 1
#
#  time = 6.7---> litres = 3
#
#  time = 11.8--> litres = 5
