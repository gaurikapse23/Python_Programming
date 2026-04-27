import numpy as np

def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

def binary_cross_entropy(actual, predicted):
    epsilon = 1e-10
    predicted = np.clip(predicted, epsilon, 1 - epsilon)
    return -np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))

def loss_demo():
    actual = np.array([1, 0, 1, 1])
    predicted = np.array([0.9, 0.2, 0.8, 0.7])

    print("MSE:", mse(actual, predicted))
    print("Binary Cross Entropy:", binary_cross_entropy(actual, predicted))

loss_demo()