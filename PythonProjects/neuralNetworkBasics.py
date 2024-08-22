# This is my first attempt at coding a neural network
# Baby steps is what it takes

import math

def sigmoid(x):
  compressor = 1/(1+math.exp(-x))
  return compressor

def neurons():
  array = []
  numberOfNeruons = 20

  for i in range(numberOfNeruons):
    activation = sigmoid(i)
    array.append(activation)
  return array

print(neurons())