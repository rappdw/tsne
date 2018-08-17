# Building & Distributing tsne-hp
tsne-mp is a binary only distribution. It is somewhat complicated to build. Because of that, we've created
a set of build scripts (in bin directory) as well as docker containers to capture all requirements for building
and for producing reproducable builds.

To build and publish:

1) Create a new release on github
2) `bin/build.sh`
3) `bin/publish.sh`

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

For the windows build you can either build natively or in a windows docker container.  

**NOTE:** Since we are using `ps1` scripts you will need to make sure you have the correct execution policy.

        #Example (Can be dangerous to make it global, use with caution)
        Set-ExecutionPolicy Bypass -Scope Process -Force

### Docker (Recommended) 

Using docker is the recommended approach and can be easily accomplished.  To complete this you will need to do the
following.  

1. Install Docker CE (>= 18.06)

2. Change Docker to [use windows containers](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)

3. (optional) Increase the [storage for windows hyper-v](https://docs.microsoft.com/en-us/visualstudio/install/build-tools-container#step-4-expand-maximum-container-disk-size)

4. Run the build `bin\build-windows.ps1`
    - If that fails, run with specific execution policy - `Set-ExecutionPolicy Bypass -Scope Process -Force; bin\build-windows.ps1`

5. Output will be in `.\dist`


### Native

This is not the recommended path, however you can setup your machine locally to build the project. I am
going to go through the instructions you will run using the [Chocolately Package Manager](https://chocolatey.org/).

**NOTE:** Since this is a ps1 script you will need to make sure you have the correct execution policy.

There are a few tools you will need to install.  

1. VS Build Tools
    - Install Visual Studio Community 2017
    - Install Build tools package (`choco install visualcpp-build-tools`)

2. Install Python (Current 3.6.6)
    - `choco install python --version 3.6.6`

3. Install Python Packages
    - (optional) Create a virtual enviornment and activate (`python -m venv .venv; .venv\Scripts\activate.bat`)
    - `pip install -r requirements.txt`

4. Install Wheel package
    - `pip install wheel`

5. Run the build
    - `.\bin\build.ps1`

6. Output will be in `.\dist`
