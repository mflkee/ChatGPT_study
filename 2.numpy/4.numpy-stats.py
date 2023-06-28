import numpy as np

#  calculating the average value of an array
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)
print(arr)
print(mean)

# calculating median array
median = np.median(arr)
print(median)

# calculating the standard deviation of an array
std_dev = np.std(arr)
print(std_dev)

# calculating the correlation between two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
correlate = np.corrcoef(a, b)
print(correlate)
