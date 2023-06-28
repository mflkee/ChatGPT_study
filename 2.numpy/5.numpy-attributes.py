import numpy as np

# return the number of dimensions of the array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)
# 2

# returns a tuple of size array
print(a.shape)
# 2,3

# returns the total number of elements in the array
print(a.size)
# 6

# returns an object describing an array
print(a.dtype)
# int32
