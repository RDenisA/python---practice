#  Solution
#  def positive_sum(arr):
#  Your code here
#  return 0
def positive_sum(arr):
    return sum(number for number in arr if number > 0)


arr = [1, -7, 7, 12]
print(positive_sum(arr))
