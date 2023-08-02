def lovefunc(flower1, flower2):
    znach1 = flower1 % 2
    znach2 = flower2 % 2
    obshee = sorted([znach1, znach2])
    return obshee == [0, 1]


print(lovefunc(2, 2))
