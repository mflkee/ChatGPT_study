import numpy as np

# This is a Python function used to return the type of the passed parameter.
# In the case of the numpy array,
# it will return numpy.ndarrayh
a = np.array([[1, 2, 3], [4, 5, 6]])
print(type(a))

# This function will create a numpy array with a given number of dimensions,
# where each element will be equal to 0
b = np.zeros((3, 3))
print(b)

# This function will create a numpy array with a given number of dimensions,
# where each element will be equal to 1.
c = np.ones((3, 3))
print(c)

# This function is used to create a numpy array whose elements lie
# in the range of values from start to stop with a difference equal to step.
d = np.arange(4, 25, 5)
print(d)

# This function will create a numpy array whose elements lie
# in the range of values between start and stop,
# and num_of_elements is the size of the array. The default type is float64.
e = np.linspace(5, 25, 5)
print(e)

# All elements are within the logarithmic scale, that is, they represent
# the logarithms of the corresponding elements.
f = np.logspace(5, 25, 5)
print(f)

# This code will return the sine of the parameter.
j = np.logspace(5, 25, 5)
print(np.sin(j))

# This function is used to change the number of dimensions of the numpy array.
k = np.arange(9). reshape(3, 3)
print(k)

# This function returns an array with a specified number of dimensions,
# where each element is randomly generated.
i = np.random.random((2, 2))
print(i)

# The function will return an ndarray with
# the exponential value of each element.
m = np.exp([10])
print(m)

# This function will return an ndarray with the square root of each element.
n = np.sqrt([16])
print(n)
