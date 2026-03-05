import matplotlib.pyplot as plt

X = [1,2,3,4,5]
Y = [20000,25000,30000,35000,40000]

n = len(X)

mean_x = sum(X)/n
mean_y = sum(Y)/n

num = 0
den = 0

for i in range(n):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2

m = num/den
c = mean_y - m*mean_x

# Predict salary for 6 years
x_new = 6
pred_salary = m*x_new + c

print("Predicted Salary for 6 Years Experience = ₹",pred_salary)

# Regression line
y_line = []

for x in X:
    y_line.append(m*x + c)

# Plot graph
plt.scatter(X,Y,label="Data Points")
plt.plot(X,y_line,label="Regression Line")

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction using Linear Regression")

plt.legend()

plt.show()