#!/usr/bin/env python3

from tsne import bh_sne
from sklearn.datasets import fetch_mldata
from shutil import copyfileobj
from six.moves import urllib
from sklearn.datasets.base import get_data_home
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def fetch_mnist(data_home=None):
    mnist_alternative_url = "https://github.com/amplab/datascience-sp14/raw/master/lab7/mldata/mnist-original.mat"
    data_home = get_data_home(data_home=data_home)
    data_home = os.path.join(data_home, 'mldata')
    if not os.path.exists(data_home):
        os.makedirs(data_home)
    mnist_save_path = os.path.join(data_home, "mnist-original.mat")
    if not os.path.exists(mnist_save_path):
        mnist_url = urllib.request.urlopen(mnist_alternative_url)
        with open(mnist_save_path, "wb") as matlab_file:
            copyfileobj(mnist_url, matlab_file)


if __name__ == '__main__':
    fetch_mnist()
    mnist = fetch_mldata("MNIST original")
    X = mnist.data
    y = mnist.target
    X_2d = bh_sne(X.astype(float))

    plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y)
    plt.savefig('test-mnist')


