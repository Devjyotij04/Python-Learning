# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(l) :
    smallest = l[0]
    for i in l :
        if i < smallest :
            smallest = i
        else :
            pass
    return smallest

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))