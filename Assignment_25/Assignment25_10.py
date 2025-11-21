"""
Q10: Split a DataFrame with multiple features into train-test for supervised learning.
data = {
'Age': [25, 30, 45, 35, 22],
'Salary': [50000, 60000, 80000, 65000, 45000],
'Purchased': [1, 0, 1, 0, 1]
}
"""

import pandas as pd
from sklearn.model_selection import train_test_split

data = {
'Age': [25, 30, 45, 35, 22],
'Salary': [50000, 60000, 80000, 65000, 45000],
'Purchased': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

print("Original DataFrame is : ")
print(df, "\n")

X = df[['Age', 'Salary']]
Y = df['Purchased']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 42)

print("DataFrame after splitting is : ")
print("X_train : \n ",X_train, "\n")
print("X_test : \n ",X_test, "\n")
print("Y_train : \n ",Y_train, "\n")
print("Y_test : \n ",Y_test, "\n")