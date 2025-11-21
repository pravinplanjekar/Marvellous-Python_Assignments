"""
Q3: Group students by gender and calculate average marks.
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

df['Total'] = df['Math'] + df['Science'] + df['English']
df['Gender'] = ['Male', 'Male', 'Female']

print(df)

Average_marks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

print(Average_marks)