#! /usr/bin/env python3

# Associative arrays aka maps
# consists of key-value-pairs.

d = dict()
print(type(d))
print(d)
print(d.keys())
print(d.values())
print(d.items())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
