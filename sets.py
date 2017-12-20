#! /usr/bin/env python3

# A set object is an unordered collection of distinct hashable objects.
# Common uses include membership testing, removing duplicates from a
# sequence, and computing mathematical operations such as an intersection,
# union, difference, and symmetric difference.

# There are currently two built-in set types, set and frozenset.
# The set type is mutable and has therefore no hash value and cannot be used
# as a dictionary key or as an element of another set.
# The frozenset type is immutable and hashable; it can therefor be used as a
# dictionary key or as an element of another set.

my_list = [1, 2, 3, 4 , 5, 1, 2, 6 ,7, 0]
print(my_list)

my_set = set(my_list)
print(my_set)

my_frozenset = frozenset(my_list)
print(my_frozenset)

my_list.append(list(range(10)))
print(my_list)
print(my_set)
print(my_frozenset)


print(set(list()))
print(frozenset(list()))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
