# List is a Python’s built-in data structure that can be used as a queue.
# append()and pop() functions are used.

'''
However, lists are quite slow for this purpose because inserting or deleting an
element at the beginning requires shifting all of the other elements by one.

'''

queue = []
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
