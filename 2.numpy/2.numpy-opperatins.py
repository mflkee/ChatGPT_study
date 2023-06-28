import numpy as np

# Arrays operations
arr1d_1 = np.array([1, 2, 3])
arr1d_2 = np.array([4, 5, 6])
# addition
a = arr1d_1 + arr1d_2

# multiplication
s = arr1d_2 * arr1d_2

# division
d = arr1d_1 * arr1d_2

# division on number
dn = arr1d_1 * 3

# transpose
t = np.array([[1, 2], [3, 4]])
g = t.T

print(a)
print(s)
print(d)
print(dn)
print(g)
