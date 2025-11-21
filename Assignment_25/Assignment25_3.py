"""
Q3: Apply Label Encoding to a 'City' column.
data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
"""

#import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

df = pd.DataFrame(data)

print("DataFrame before encoding : ")
print(df)

LE = LabelEncoder()
df['City_Encoded'] = LE.fit_transform(df['City'])

print("DataFrame after encoding : ")
print(df)

