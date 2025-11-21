"""
Q7: Normalize 'Age' column using Min-Max Scaling.
data = {'Age': [18, 22, 25, 30, 35]}
"""

import pandas as pd

data = {'Age': [18, 22, 25, 30, 35]}

df = pd.DataFrame(data)

print(df)

min_age = df['Age'].min()
max_age = df['Age'].max()

df['Age_Normalized'] = (df['Age'] - min_age) / (max_age - min_age)

print(df)