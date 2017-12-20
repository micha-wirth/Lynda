# Arrays with one dimension.
my_array1 = list()
my_array2 = []

my_array1.extend(range(8))
my_array2.extend(list(range(8)))

print(my_array1)
print(my_array2)

# Arrays with multiple dimensions.
my_array3 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

my_array4 = [[i for i in range(3)] for i in range(3)]

print(my_array3)
print(my_array4)

# Arrays with multiple arrays.


# list.append(value)
# list.insert(index, value)
# list.pop(index)
# list.remove(object)

