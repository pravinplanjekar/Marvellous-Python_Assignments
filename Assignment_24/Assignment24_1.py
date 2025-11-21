"""
Q1: Normalize the 'Math' scores using Min-Max scaling.
"""

from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([85,90,78]).reshape(-1,1)

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(data)

print(scaled_data)