"""# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => "" """

def encrypt_message(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = ""
    for i in s :
        pos = (a.index(i) + 2) % 26
        b += a[pos]
    return b

print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))