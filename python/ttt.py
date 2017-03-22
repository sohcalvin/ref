import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

print(sigmoid(6))
print(sigmoid(7))
print(sigmoid(20))

tmp1 = softmax([5,6,5.5])
tmp2 = softmax([2.7,2.8,4.2,])
tmp3 = softmax([9.7,9.8,6.4])
