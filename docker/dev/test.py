#!/usr/bin/env python3

from sklearn.datasets import load_iris
from tsne import bh_sne
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data
y = iris.target
X_2d = bh_sne(X)
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y)
plt.savefig('test')