#! /usr/bin/env python3

# Hash functions return the hash value of the object.
# Hash values are integers. They are used to quickly compare
# dictionary keys during a dictionary lookup.
# Numeric values that compare equal have the same hash value.

my_object1 = int(10)
my_object2 = float(10)

print('Hash value of', my_object1, '-->', hash(my_object1))
print('Hash value of', my_object2, '-->', hash(my_object2))


# Secure hash.
import  hashlib
my_hash = hashlib.new('ripemd160')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
