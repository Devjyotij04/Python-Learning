# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True

def beginning_and_end(l) :
    if l[0] == l[-1] :
        return True
    else :
        return False
    

print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))
print(beginning_and_end(["a", "b", "a"]))
print(beginning_and_end([15]))