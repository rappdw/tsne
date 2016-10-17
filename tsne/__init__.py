# encoding: utf-8
from __future__ import division
import numpy as np
import scipy.linalg as la
import sys
from bh_sne import BH_SNE
from bh_sne_3d import BH_SNE_3D

def bh_sne(data, pca_d=None, d=2, perplexity=30., theta=0.5,
           random_state=None, copy_data=False, init=None,
           max_iter=None, stop_lying_iter=None, mom_switch_iter=None):
    """
    Run Barnes-Hut T-SNE on _data_.

    @param data         The data.

    @param pca_d        The dimensionality of data is reduced via PCA
                        to this dimensionality.

    @param d            The embedding dimensionality. Must be 2 or 3.

    @param perplexity   The perplexity controls the effective number of
                        neighbors.

    @param theta        If set to 0, exact t-SNE is run, which takes
                        very long for dataset > 5000 samples.

    @param random_state A numpy RandomState object; if None, use
                        the numpy.random singleton. Init the RandomState
                        with a fixed seed to obtain consistent results
                        from run to run.

    @param copy_data    Copy the data to prevent it from being modified
                        by the C code

    @param init         Numpy array of initial positions

    @param max_iter    Maximum number of iterations

    @param stop_lying_iter Iterations spent in high-alpha mode

    @param mom_switch_iter Iterations spent in high-momentum mode
    """
    N, _ = data.shape

    if pca_d is None:
        if copy_data:
            X = np.copy(data)
        else:
            X = data
    else:
        # do PCA
        data -= data.mean(axis=0)

        # working with covariance + (svd on cov.) is
        # much faster than svd on data directly.
        cov = np.dot(data.T, data) / N
        u, s, v = la.svd(cov, full_matrices=False)
        u = u[:, 0:pca_d]
        X = np.dot(data, u)

    if random_state is None:
        seed = np.random.randint(2**31-1)
    else:
        seed = random_state.randint(2**31-1)

    if init is None:
        use_init = False
        init = np.zeros((1, d))
    else:
        use_init = True

    if max_iter is None:
        max_iter = 1000

    if stop_lying_iter is None:
        stop_lying_iter = 250

    if mom_switch_iter is None:
        mom_switch_iter = 250

    if d == 2:
        tsne = BH_SNE()
    elif d == 3:
        tsne = BH_SNE_3D()
    else:
        raise Exception("TSNE dimensions must be 2 or 3")

    Y = tsne.run(X, N, X.shape[1], d, perplexity, theta, seed, init=init, use_init=use_init,
                 max_iter=max_iter, stop_lying_iter=stop_lying_iter, mom_switch_iter=mom_switch_iter)
    return Y

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
