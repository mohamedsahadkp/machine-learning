import numpy as np


# Hyperparameter
feature = np.array([1, 3])
label = np.array(4)
weight = np.array([0.2, 0.4])

learingRate = 0.001

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def devSigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Apply activation function
output =  sigmoid(np.dot(feature, weight))

#Find error
error = label - output 

#Gradient Decent
gradient = learingRate * error * devSigmoid(np.dot(feature, weight)) * feature

# Result
print gradient



