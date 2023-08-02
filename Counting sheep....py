def count_sheeps(sheep):
    return sheep.count(True) + 0


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))
