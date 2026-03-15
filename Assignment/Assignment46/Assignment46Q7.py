from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([50,55,60,65,70])

model = LinearRegression()

model.fit(X,y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)