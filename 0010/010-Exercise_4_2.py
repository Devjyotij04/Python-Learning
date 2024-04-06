# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0


def sum_of_values_and_indices(l) :
    v = enumerate(l)
    j = 0
   
    for i,e in v :
        j = j+i+e
       
    return j

print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))