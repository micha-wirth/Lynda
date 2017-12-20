#! /usr/bin/env python3

# Hash tables
my_object1 = 123
my_object2 = my_object1
my_object3 = 123

print(hash(my_object1))
print(hash(my_object2))
print(hash(my_object3))

my_object4 = 'Wahleim'
my_object5 = 'Walheim'
my_object6 = my_object4
print(hash(my_object4))
print(hash(my_object5))
print(hash(my_object6))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
