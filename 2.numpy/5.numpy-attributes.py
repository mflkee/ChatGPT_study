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

# Returns the size of each element in the array in bytes
print(a.itemsize)
# 4 , 32/8 = 4

# Returns a buffer with the current array elements.
# This is an alternative way to access elements through their indexes
print(a.data)
# elements array

# The function will return the sum of all the elements of ndarray
b = np.random.random((2, 3))
print(b)
print(b.sum())

# The function will return the element with the minimum value from ndarray.
print(b.min())

# The function will return the element with the minimum value from ndarray.
print(b.max())
