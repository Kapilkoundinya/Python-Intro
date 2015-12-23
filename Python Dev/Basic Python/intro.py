"""
List - Ordered
Tuples - Ordered
Dictionary - Unordered
Set - Unordered

 - Tuples can be used as keys in dictionaries and elements of sets
"""

# Containers
s_List = [1, 1, 1]  # List - An ordered collection of elements of different types (need not to be distinct)
s_Set = {1, 1, 1, 4}  # Set - An unordered collection of distinct elements
s_Dict = {0: 1, 1: 2, 2: 3}  # Dictionary - (key, value) based data storage where keys can be changed
s_tuple = (1, 2, 3)  # Tuple - An immutable ordered list of values


'''
s = [1, 1, 1]
s[2] = "foo"
print s

s.append(3)
print(s)

# For loop
animals = ["cat", "pat", "meat"]
for ind, animal in enumerate(animals):
    print "#%d : %s" % (ind, animal)

# List comprehension
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
even_squares = [x**2 for x in nums if x % 2 == 0]
print(squares)
print(even_squares)

# Dictionary
d = {'cat': 'animal', 'human': 'mamal'}
print d.get('cat', 'N/A')

for animal in d:
    category = d[animal]
    print '%s belongs to % s category' % (animal, category)

for category, animal in d.iteritems():
    print '%s belongs to % s category' % (animal, category)

# Sets
setss = {'cat', 'ball', 'dog'}
setss.add('cat')
print(setss)

for setElements in setss:
    print(setElements)

dict = {(x, x+1): x for x in range(30)}
print(dict)
tup = (5, 6)
print dict[tup]

'''


class Greeter:

    def __init__(self, name):
        self.name = name

    def greeting(self, loud=False):

        if loud == False:
            print("Hello %s" % self.name)

        else:
            print("HELLO %s" % self.name.upper())

g = Greeter('freedy')
g.greeting()
g.greeting(loud=True)
