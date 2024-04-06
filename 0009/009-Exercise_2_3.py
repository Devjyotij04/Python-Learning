# Define a first_letter_of_last_string function that accepts a list of strings. 
# It should return one character — the first letter of the last string in the list. 
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
# first_letter_of_last_string(["nonsense"]) => "n"


def first_letter_of_last_string(l) :
    return l[-1][0]


print(first_letter_of_last_string(["cat", "dog", "zebra"]))
print(first_letter_of_last_string(["nonsense"]))