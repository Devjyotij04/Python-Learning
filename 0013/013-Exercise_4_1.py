# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = []
for value in values :
    floats.append(float(value))
print(floats)

# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = []
for letter in name :
    letters.append(letter*3)
print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = []
for element in elements :
    lengths.append(len(element))

print(lengths)