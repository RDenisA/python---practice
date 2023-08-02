def square_sum(numbers):
    res = []
    for number in numbers:
        number = number ** 2
        res.append(number)
    return sum(res)


print(square_sum([0, 3, 4, 5]))
