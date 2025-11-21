"""
Q6: Replace multiple values in a column using a dictionary.
data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
Replace as
'A+': ‘Excellent'
'A': 'Very Good’
'B+': ‘Good'
'B': ‘Average'
'C': 'Poor'
"""

import pandas as pd

data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

df = pd.DataFrame(data)

print(df)

new_dict = {
    'A+': 'Excellent',
    'A': 'Very Good',
    'B+': 'Good',
    'B': 'Average',
    'C': 'Poor'
}

df['Grade'] = df['Grade'].replace(new_dict)

print(df)