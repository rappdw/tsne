# distutils: language = c++
import numpy as np
cimport numpy as np
cimport cython
from libcpp cimport bool

cdef extern from "tsne.h":
    cdef cppclass TSNE:
        TSNE()
        void run(double* X, int N, int D, double* Y, int no_dims, double perplexity, double theta, int rand_seed, bool skip_random_init, double *init, bool use_init, int max_iter, int stop_lying_iter, int mom_switch_iter)

cdef class BH_SNE_3D:
    cdef TSNE* thisptr # hold a C++ instance

    def __cinit__(self):
        self.thisptr = new TSNE()

    def __dealloc__(self):
        del self.thisptr

    @cython.boundscheck(False)
    @cython.wraparound(False)
    def run(self, X, N, D, d, perplexity, theta, seed, init, use_init, max_iter, stop_lying_iter, mom_switch_iter):
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] _X = np.ascontiguousarray(X)
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] _init = np.ascontiguousarray(init)
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] Y = np.zeros((N, d), dtype=np.float64)
        self.thisptr.run(&_X[0,0], N, D, &Y[0,0], d, perplexity, theta, seed, False, &_init[0,0], use_init, max_iter, stop_lying_iter, mom_switch_iter)
        return Y
