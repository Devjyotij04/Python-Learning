# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]


def split_in_two(l,n):
    if n%2 == 0 :
        return l[2:]
    else :
        return l[0:2]
    
values = ["a", "b", "c", "d", "e", "f"]
print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))