def basic_op(operator, value1, value2):
    if operator == '+': return value1 + value2
    if operator == '-': return value1 - value2
    if operator == '*': return value1 * value2
    if operator == '/': return value1 / value2


print(basic_op('-', 15, 18))

#  ('+', 4, 7) --> 11
#  ('-', 15, 18) --> -3
#  ('*', 5, 5) --> 25
#  ('/', 49, 7) --> 7
