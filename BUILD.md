# Building & Distributing tsne-hp
tsne-mp is a binary only distribution. It is somewhat complicated to build. Because of that, we've created
a set of build scripts (in bin directory) as well as docker containers to capture all requirements for building
and for producing reproducable builds.

## Build Prerequisites

* [numpy](numpy.scipy.org)
* [scipy](http://www.scipy.org/)
* [cython](cython.org)
* [cblas](http://www.netlib.org/blas/) or [openblas](https://github.com/xianyi/OpenBLAS). Tested version is v0.2.5 and v0.2.6 (not necessary for OSX).
* [OpenMp](http://www.openmp.org/)


## Linux

Run `bin/build-linux.sh`. This will produce manylinux wheels for python 3.5 - 3.7 (in wheelhouse directory)

## OSX

See [this blog post](https://iscinumpy.gitlab.io/post/omp-on-high-sierra/)
* `brew install libomp`
* install pipenv
* add necessary args to compile_args and link_args in setup.py for platform == 'darwin' (these have been added to setup.py)
* Run `bin/build-osx.sh`. This will produce osx wheels for python 3.5 - 3.7 (in dist)

## Windows

Nothing Yet



