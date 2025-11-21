"""
Q4: Plot a pie chart of subject marks for 'Sagar'.
"""

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

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

Sagar_Data = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].values.flatten()
Subjects = ['Math','Science', 'English']

plt.figure(figsize=(8,8))
plt.pie(
    Sagar_Data,
    labels=Subjects,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Subject-wise Marks for Sagar")
plt.show()