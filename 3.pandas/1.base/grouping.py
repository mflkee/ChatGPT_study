import pandas as pd
from creating import df

# Grouping data and performing aggregation functions
grouped_data = df.groupby('study')['age'].mean()
print(grouped_data)
