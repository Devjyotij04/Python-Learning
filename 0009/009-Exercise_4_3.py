# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(l,s) :
    if s in l and len(s) > 4 :
        return True
    else :
        return False
    
words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "rhino"))
print(long_word_in_collection(words, "cat"))
print(long_word_in_collection(words, "monkey"))