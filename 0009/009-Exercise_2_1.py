# Define a first_and_last function that accepts a list of strings. 
# The function should return a concatenation of the first element and the last element. 
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])        => "ac"
# first_and_last(["bob", "tom", "rob"])  => "bobrob"
# first_and_last(["a"])                  => "aa"

def first_and_last(l) :
    return l[0] + l[-1]


print(first_and_last(["a", "b", "c"]))
print(first_and_last(["bob", "tom", "rob"]))
print(first_and_last(["a"]))