def century(year):
    century = year // 100
    if year % 100 == 0:
        return century
    return century + 1


print(century(87))
