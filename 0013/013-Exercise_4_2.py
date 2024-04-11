# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(lst1, lst2) :
    diff = []
    for l1 in lst1 :
        if l1 not in lst2 :
            diff.append(l1)
    return diff
        
print(destroy_elements([1, 2, 3], [1, 2]) )
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))