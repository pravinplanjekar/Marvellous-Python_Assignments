"""
Q8: Fill missing values in a numeric column using interpolation.
data = {'Marks': [85, np.nan, 90, np.nan, 95]}
"""

import pandas as pd
import numpy as np

data = {'Marks': [85, np.nan, 90, np.nan, 95]}

df = pd.DataFrame(data)

print("Original DataFrame is : ")
print(df)

df['Marks'] = df['Marks'].interpolate(method='linear')

print("DatFrame after interpolation is : ")
print(df)