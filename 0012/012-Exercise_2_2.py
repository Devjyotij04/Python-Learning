# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42


def sum_from(n1,n2) :
    l = list(range(n1,n2+1))
    s = 0
    for i in l :
        s += i
    return s

print(sum_from(1, 2))
print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12))