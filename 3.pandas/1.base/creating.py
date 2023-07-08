import pandas as pd
# creating siries
s = pd.Series([1, 2, 3, 5, 7, 9])
print(s)

# creating DataFrame
data = {
    'name': ['Gleb', 'Boris', 'Katya', 'Vera'],
    'age': [25, 56, 46, 12],
    'study': ['Hight', 'Shcool', 'Hight', 'Shcool']
}
df = pd.DataFrame(data)
print(df)
