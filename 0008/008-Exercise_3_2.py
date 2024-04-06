# Declare a string_theory function that accepts a string as an argument. 
# It should return True if the string has more than 3 characters 
# and starts with a capital “S”. It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

def string_theory(s):
    if len(s) > 3 and s[0] == 'S' :
        return True
    else :
        return False
    
print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))