# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"

def even_or_odd(n):
    if n%2 == 0 :
        return "even"
    else :
        return "odd"

v1 = even_or_odd(2)
v2 = even_or_odd(0)
v3 = even_or_odd(13)
v4 = even_or_odd(9)

print(v1)
print(v2)
print(v3)
print(v4)