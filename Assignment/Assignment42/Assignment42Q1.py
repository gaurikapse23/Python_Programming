# Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

n = len(X)

# Mean of X
mean_x = sum(X)/n

# Mean of Y
mean_y = sum(Y)/n

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# Calculate slope
num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# Intercept
c = mean_y - m * mean_x

print("Slope (m) =", round(m,2))
print("Intercept (c) =", round(c,2))

print("\nRegression Equation:")
print("Y =", round(m,2),"X +",round(c,2))

# Prediction for X = 6
x_new = 6
y_pred = m*x_new + c

print("\nPredicted Y for X = 6 =", round(y_pred,2))