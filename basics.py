# Strings


# Integers


# Doubles


# Lists
# General purpose
# Most widely used data structure
# Grown and shrink size as needed
# Sequence type
# Sortable


# Dicts
# Key/Value pairs
# Associative array, like Java HashMap
# Unordered

# Set
# Store non-duplicate items
# Very fast access vs. lists
# Math set ops (union, intersect, disjoint)
# Unordered

# Tuple
# Immutable
# Useful for fixed data
# Faster than lists
# Sequence type

# ex_tup = (1, 3, 2, 5, 6, 7)
# print(ex_tup.count(1))


# Sequences (String, List, Tuple) support:
# indexing
# Slicing
# Adding/Concatenating
# Multiplying
# Checking membership
# Iterating
# len(), min(), max(), sum(), sorted(), sequence1.count(item), sequence1.index(item)


# Classes (OOP)
class Person(object):
    total = 0

    def __init__(self, name):
        self.name = name
        Person.increment_population(1)

    def introduction(self):
        print("Hello, my name is {}".format(self.name))

    @staticmethod
    def total_population():
        print("Total population is {}".format(Person.total))

    @staticmethod
    def increment_population(number=1):
        Person.total += number


Person.total_population()
vlad = Person(name="Vlad")
vlad.introduction()
Person.total_population()
