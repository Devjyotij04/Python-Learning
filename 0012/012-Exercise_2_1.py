# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))  

def length_match(l,i) :
    n = 0
    for j in l :
        if len(j) == i :
            n+=1
    if n > 0 :
        return n
    else :
        return 0
    
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([],5))