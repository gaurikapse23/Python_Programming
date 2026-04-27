import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def artificial_neuron():
    x1, x2 = 2, 3
    w1, w2 = 0.4, 0.6
    bias = 0.5

    z = (x1 * w1) + (x2 * w2) + bias
    output = sigmoid(z)

    print("Weighted Sum (Z):", z)
    print("Final Output:", output)

    if output > 0.5:
        print("Output is closer to 1")
    else:
        print("Output is closer to 0")

artificial_neuron()