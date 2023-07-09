import pandas as pd
from creating import df

# Selecting data by index:
print(df.loc[2])

# Selecting data by columns:
print(df['name'])

# Selecting data by condition:
print(df[df['age'] < 30])
