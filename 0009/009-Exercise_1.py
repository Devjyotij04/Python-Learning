# Create an empty list and assign it to the variable "empty".


# Create a list with a single Boolean — True — and assign it to the variable "active".


# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".


# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".


# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

empty = []
active = [True]
favorite_numbers = [3,4,6,7,8]
colors = ["red", "green", "blue"]

def is_long(l) :
    if len(l) > 5 :
        return True
    else :
        return False
    
a = is_long(favorite_numbers)

print(a)
