# coding: utf-8

import sys, os
sys.path.append(os.pardir)
import numpy as np
from deeplearning_bases.common.functions import softmax, cross_entropy_error
from deeplearning_bases.common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.rand(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        _loss = cross_entropy_error(y, t)

        return _loss

x = np.random.rand(2)
t = np.array([0,0,1])

net = simpleNet()

f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print(dW)
