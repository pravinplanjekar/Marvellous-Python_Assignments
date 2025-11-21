"""
Q9: Replace values in 'Marks' less than 50 with 'Fail' using where().
data = {'Marks': [45, 67, 88, 32, 76]}
"""

import pandas as pd

data = {'Marks': [45, 67, 88, 32, 76]}

df = pd.DataFrame(data)

print("Original DataFrame is : ")
print(df)

df['Marks'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')

print("DataFrame after replacement : ")

print(df)