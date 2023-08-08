def reverse_seq(n):
    result = []
    for integer in range(n, 0, -1):
        result.append(integer)
    result.sort(reverse=True)
    return result


print(reverse_seq(5))
