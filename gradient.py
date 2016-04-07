import numpy as np

X = np.matrix('0.1;0.25;0.5;0.75;1')
y = np.matrix('0;0;0;0;0')

# "Randomly" initialize the weight
weight = np.matrix('5.0')

def sigmoid(x):
    return np.matrix(1.0 / (1.0 + np.exp(-x)))

def run(X, weight):
    return sigmoid(X * weight)

def cost(X, y, weight):
    h = run(X, weight)
    m = X.shape[0]
    return np.sum(np.square(h - y)) / (2 * m)

def cost_derivative(X, y, weight):
    h = run(X, weight)
    m = X.shape[0]
    return np.sum(np.multiply((h - y), np.multiply(h, (1 - h))))

alpha = 0.5
epochs = 2000

print(cost(X, y, weight))
for i in range(epochs):
    slope = cost_derivative(X, y, weight)
    weight = weight - alpha * slope

print(cost(X, y, weight))
print weight
print(X * weight)
print(np.round(run(X, weight), 1))
