import numpy as np

# Define an array with some elements that are zero and some that are non-zero
array = np.array([0, 0, 0, 1, 0, 0])

# Test whether any of the elements in the array are non-zero
result = np.any(array)

print(result)