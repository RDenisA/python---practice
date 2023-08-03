def digitize(n):
    n = str(n)
    result = []
    for integer in n:
        result.append((int(integer)))
    return list(reversed(result))


print(digitize(35231))


#  my_list = [10,20,30,40,50]
#  my_list.reverse()
#  print("This is what the list looks like now: ", my_list)


#  35231 => [1,3,2,5,3]
#  0 => [0]
