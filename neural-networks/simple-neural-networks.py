import numpy as np

input = np.array([0.2, -0.3])
weight = np.array([0.01, 0.02]) 
bais = 0.01

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

output = sigmoid(np.dot(input, weight) + bais)

print output
