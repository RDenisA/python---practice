def converter(mpg):
    kpg = mpg * 1.609344
    lpk = kpg / 4.54609188
    return round(lpk, 2)


print(converter(12))
