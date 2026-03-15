from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
[1,7],
[2,6],
[3,7],
[4,6],
[5,8]
])

y = np.array([50,55,60,65,70])

model = LinearRegression()

model.fit(X,y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)