"""
Q2: Detect column data types and convert 'Age' from float to int.
data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
"""

import numpy as np
import pandas as pd

data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

df = pd.DataFrame(data)

print("DataFrame before convesion is : ")
print(df)

#print(df.dtypes)

df['Age'] = df['Age'].astype(int)

print("DataFrame after convesion is : ")
print(df)

#print(df.dtypes)