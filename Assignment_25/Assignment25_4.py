"""
QQ4: Apply One-Hot Encoding to a 'Department' column.
data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
"""

import pandas as pd

data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

df = pd.DataFrame(data)

print(df)

df_encoded = pd.get_dummies(df, columns=['Department']).astype(int)

print(df_encoded)