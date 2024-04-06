# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(n) :
    if n > 0 :
        return n
    else :
        return -1*n
    
print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))