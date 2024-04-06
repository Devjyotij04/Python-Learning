# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(l) :
    s = 0
    for i in l :
        if 's' in i :
            s = s+i.index('s')
        else :
            pass
            
    return s

print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))