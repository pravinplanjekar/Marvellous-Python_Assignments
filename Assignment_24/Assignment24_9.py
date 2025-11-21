"""
Q9: Rename 'Math' column to 'Mathematics'.
"""

import pandas as pd

data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science'] + df['English']
df['Gender'] = ['Male', 'Male', 'Female']

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

Passed_Count = df['Status'].value_counts()['Pass']
print("Number of passed students are:", Passed_Count)

print(df)

df.rename(columns={'Math': 'Mathematics'}, inplace=True)

print(df)


