# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []


def long_strings(texts) :
    ls = []
    for text in texts :
        if len(text) >= 5 :
            ls.append(text)
    return ls

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))