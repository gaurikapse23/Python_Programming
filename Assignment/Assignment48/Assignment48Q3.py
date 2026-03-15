from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[25,20000],
                 [30,40000],
                 [35,80000]])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)

print("Original Data:")
print(data)

print("\nScaled Data:")
print(scaled_data)