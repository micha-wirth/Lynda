#! /usr/bin/env python3

# Heap queue algorithm aka priority queue algorithm.
# Heaps are binary trees for which every parent node has a value less then or equal to any of its children.
# This implementation uses array for which heap[k] <= heap[2*k+1] and heap[2*k+2] for all k, counting from zero.

# A priority queue is a common use for a heap, and it presents several implementation challenges:

import heapq

def heapsort(iterable):
    """
    Heap sort algorithm

    >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    :param iterable:
    :return:
    """
    my_heap = []
    for value in iterable:
        heapq.heappush(my_heap, value)
    return [heapq.heappop(my_heap) for i in range(len(my_heap))]

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(data)
heapq.heapify(data)
print(data)
[heapq.heappop(data) for i in range(len(data))]
print(data)



if __name__ == "__main__":
    import doctest

    doctest.testmod()