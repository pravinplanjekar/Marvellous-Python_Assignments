"""
Q1: Create a DataFrame for student marks and print basic information like shape, columns, and
data types.
data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}
Note : Consider the same dataset for this as well as next assignment.
"""

import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}

df = pd.DataFrame(data)
print(df)

print("Shape : ",df.shape)
print("Columns : ",df.columns)
print("Datatypes : ",df.dtypes)