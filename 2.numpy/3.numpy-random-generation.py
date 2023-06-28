import numpy as np

# generation random number
random_num = np.random.rand()

# generation random array
random_arr = np.random.rand(3, 3)

# Generating a random array with an average value and standard deviation
mean = 0
std_dev = 1
random_arr2 = np.random.normal(mean, std_dev, (3, 3))

print(random_num)
print(random_arr)
print(random_arr2)
