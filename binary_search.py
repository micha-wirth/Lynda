# Divide-and-conquer algorithm
def divide_and_conquer(arr, val):
    lower_bound = 0
    upper_bound = len(arr) - 1
    ret_val = None

    index = (lower_bound + upper_bound) // 2

    while lower_bound <= upper_bound:
        if arr[index] < val:
            lower_bound = index + 1
        elif arr[index] > val:
            upper_bound = index - 1
        else:
            ret_val = index
            break
        index = (lower_bound + upper_bound) // 2

    return ret_val


my_array = list(range(10, 21, 1))
print(my_array)
index = divide_and_conquer(my_array, 9)
print(index)

