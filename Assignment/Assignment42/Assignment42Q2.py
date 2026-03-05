X = [1,2,3,4,5]
Y = [3,4,2,4,5]

m = 0.4
c = 2.4

# Predicted Y values
y_pred = []

for x in X:
    y_pred.append(m*x + c)

print("Predicted Y values:", y_pred)

# MSE calculation
error_sum = 0

for i in range(len(Y)):
    error_sum += (Y[i] - y_pred[i])**2

mse = error_sum/len(Y)

print("Mean Squared Error =", round(mse,2))

# R2 Score

mean_y = sum(Y)/len(Y)

ss_total = 0
ss_res = 0

for i in range(len(Y)):
    ss_total += (Y[i] - mean_y)**2
    ss_res += (Y[i] - y_pred[i])**2

r2 = 1 - (ss_res/ss_total)

print("R2 Score =", round(r2,2))