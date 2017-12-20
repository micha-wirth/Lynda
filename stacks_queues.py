#! /usr/bin/env python3

"""
Stack: "last-in-first-out".
List methods make it very easy to use a list as a stack.
To add an item to the top of the stack, use append().
To retrieve an item form the top of the stack, use pop()
without an explicit index.
"""
stack = [3, 4, 5]
print(stack)
stack.append(6)
print(stack)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

"""
Queue: "First-in-first-out".
Lists are not efficient for using it as queue.
To implement a queue, use collections.deque which was
designed to have fast appends and pops from both ends.
It is an alternative implementation of unbounded queues

with fast atomic append() and popleft() operations
that do not require locking.
"""
from collections import deque
queue = deque([3, 4, 5])
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

"""
The queue module implements multi-producer, multi-consumer queues.
It is especially useful in threaded programming when information
must be exchanged safely between multiple threads.

The module implements three types of queue:
FIFO queue, LIFO queue and a priority queue.

"""
import queue

fifo = queue.Queue()
print(fifo)
fifo.put(3)
fifo.put(4)
fifo.put(5)
print(fifo.get())
print(fifo.get())
print(fifo.get())

lifo = queue.LifoQueue()
print(lifo)
lifo.put(3)
lifo.put(4)
lifo.put(5)
print(lifo.get())
print(lifo.get())
print(lifo.get())

prio = queue.PriorityQueue()
print(prio)
prio.put((2, 'data 3'))
prio.put((1, 'date 4'))
prio.put((5, 'data 5'))
prio.put((0, 'data 6'))
print(prio.get())
print(prio.get())
print(prio.get())
