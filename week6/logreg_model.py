
import numpy as np

def sigmoid(z):
    # Calculate the sigmoid
    sig = 1. / (1. + np.exp(-z))
    #sig = 1. / (1. + np.exp(-np.clip(logits,-100,100)))
    return sig

def NLL_batch_gradient_descent(X,y,weights,learning_rate,n_iterations):
    # Perform gradient descent to calculate weights that minimize the NLL cost function
    epsilon = 1e-10 # Add tiny value to avoid getting nan values from log(0)
    cost_path = []
    for i in range(n_iterations):
        # Calculate the cost
        z = X.dot(weights)
        cost = -np.sum(y*(np.log(sigmoid(z)+epsilon))+(1.-y)*(np.log(1.-sigmoid(z)+epsilon)))
        # OR USE LINALG: cost = -(y.dot(np.log(sigmoid(z)+epsilon))+(1.-y).dot(np.log(1.-sigmoid(z)+epsilon)))
        cost_path.append(cost)
        # Calculate the gradient
        gradient = -X.T.dot(y-sigmoid(z))
        # Adjust the weights, moving in the direction opposite the gradient
        weights = weights - learning_rate * gradient
    return weights,cost_path