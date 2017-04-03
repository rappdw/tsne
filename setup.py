"""
To upload a new version:
1. make clean
2. git tag a new version: git tag v1.x.x
3. python setup.py bdist_wheel
4. python setup.py bdist_wheel upload -r pypi-internal
"""

import sys
import os
import platform
import shutil

from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension
from distutils.dir_util import copy_tree

import versioneer
import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize


class CmakeBuildMixin():
    def cmake_build(self):
        build_dir = os.path.join(os.path.dirname(__file__), self.build_lib + '/cmake')
        source_dir = os.path.join(os.path.join(os.path.dirname(__file__), 'tsne'), 'bh_sne_src')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
        else:
            shutil.rmtree(build_dir)
            os.makedirs(build_dir)

        cwd = os.getcwd()
        try:
            os.chdir(build_dir)
            return_val = os.system('cmake -DCMAKE_BUILD_TYPE=RELEASE ' + source_dir)

            if return_val != 0:
                print('cannot find cmake')
                exit(-1)

            os.system('make VERBOSE=1')
            # delete any of the cmake generated files
            shutil.rmtree(os.path.join(build_dir, 'CMakeFiles'))
            os.remove(os.path.join(build_dir, 'CMakeCache.txt'))
            os.remove(os.path.join(build_dir, 'Makefile'))
            os.remove(os.path.join(build_dir, 'cmake_install.cmake'))
            # this leaves just the generated executables in the path.
            # copy them into the tsne directory so that they will be picked
            # up by the install_lib command during install, or bdist_wheel
            dest_dir = os.path.join(os.path.dirname(build_dir), 'tsne')
            copy_tree(build_dir, dest_dir)
        finally:
            os.chdir(cwd)
            shutil.rmtree(build_dir)


class CmakeBuildExt(CmakeBuildMixin, build_ext):
    def run(self):
        build_ext.run(self)
        self.cmake_build()


if sys.platform == 'darwin':
    # OS X
    version, _, _ = platform.mac_ver()
    parts = version.split('.')
    v1 = int(parts[0])
    v2 = int(parts[1])
    v3 = int(parts[2]) if len(parts) == 3 else None

    ext_modules = [Extension(name='tsne.bh_sne',
                             sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                             include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                             extra_compile_args=['-ffast-math', '-fopenmp', '-flto'],
                             extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lgomp'],
                             language='c++'),

                   Extension(name='tsne.bh_sne_3d',
                             sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne_3d.pyx'],
                             include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                             extra_compile_args=['-ffast-math', '-DTSNE3D', '-fopenmp', '-flto'],
                             extra_link_args=['-Wl,-framework', '-Wl,Accelerate', '-lgomp'],
                             language='c++')]

else:
    # LINUX
    ext_modules = [Extension(name='tsne.bh_sne',
                             sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                             include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                             library_dirs=['/usr/local/lib', '/usr/lib64/atlas'],
                             extra_compile_args=['-msse2', '-fPIC', '-w', '-ffast-math', '-O2', '-fopenmp', '-flto'],
                             extra_link_args=['-lgomp'],
                             language='c++'),

                   Extension(name='tsne.bh_sne_3d',
                             sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne_3d.pyx'],
                             include_dirs=[numpy.get_include(), '/usr/local/include', 'tsne/bh_sne_src/'],
                             library_dirs=['/usr/local/lib', '/usr/lib64/atlas'],
                             extra_compile_args=['-msse2', '-fPIC', '-w', '-ffast-math', '-DTSNE3D', '-O2', '-fopenmp',
                                                 '-flto'],
                             extra_link_args=['-lgomp'],
                             language='c++')]

ext_modules = cythonize(ext_modules)

cmdclass = versioneer.get_cmdclass()
cmdclass['build_ext'] = CmakeBuildExt # build_ext

setup(name='tsne',
      version=versioneer.get_version(),
      cmdclass=cmdclass,
      author='Daniel Rapp',
      author_email='rappdw@gmail.com',
      url='https://github.com/rappdw/tsne.git',
      description='TSNE implementations for python',
      long_description='''
This is based on the https://github.com/10XDev/tsne.git fork of L.J.P. van der Maaten BH-tSNE implementation.

It has fixes to allow this to run in Python 3. More significantly, performance has been significantly
increased with OpenMP parallelism (see: https://github.com/rappdw/tsne-perf-test.git)''',
      license='Apache License Version 2.0, January 2004',
      packages=find_packages(),
      ext_modules=ext_modules,
      install_requires=[
          'numpy',
          'scipy'
          ]
      )
