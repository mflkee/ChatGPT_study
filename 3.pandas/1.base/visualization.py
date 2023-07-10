import pandas as pd
import matplotlib.pyplot as plt

data = {'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        'sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]}

df = pd.DataFrame(data)

df.plot(x='year', y='sales', kind='line')
plt.show()


data = {'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

df.plot(x='x', y='y', kind='scatter')
plt.show()
