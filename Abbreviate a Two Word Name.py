def abbrev_name(name):
    words = name.split(' ')
    letters = [word[0]. upper() for word in words]
    return '.'.join(letters)


print(abbrev_name("Sam Harris"))
