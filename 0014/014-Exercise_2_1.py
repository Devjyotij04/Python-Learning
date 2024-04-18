# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

def greater_sum(numbers1, numbers2) :
    if sum(numbers1) > sum(numbers2) :
        return numbers1
    else :
        return numbers2

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

