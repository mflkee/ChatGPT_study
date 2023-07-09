import pandas as pd
from creating import df
# Basic methods of working with a data frame, such as
# head(), tail(), shape, info(), describe():

# head()
# returns the first few rows of the Data Frame (5 rows by default).
print(df.head(2))
print()

# tail()
# returns the last few rows of the Data Frame (5 rows by default).
print(df.tail(2))

# shape
# returns a tuple containing the number of rows and columns in the Data Frame.
print(df.shape)

# info()
# displays information about the DataFrame, including the number of rows and
# columns, the presence of missing data, and column data types.
print(df.info())

# describe()
# outputs statistical characteristics of the data in the Data Frame, such as
# the mean value, standard deviation, minimum and maximum values, and others.
print(df.describe())
