def fake_bin(x):
    binary_string = ''
    for number in x:
        if int(number) < 5:
            binary_string += '0'
        else:
            binary_string += '1'
    return binary_string


print(fake_bin("45385593107843568"))
