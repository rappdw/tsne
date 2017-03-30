"""
To upload a new version:
1. make clean
2. git tag a new version: git tag v1.x.x
3. python setup.py sdist
4. python setup.py sdist register upload
"""

import sys
import platform

from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension

import versioneer
import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize

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

with open('requirements.txt') as f:
    required = f.read().splitlines()

cmdclass = versioneer.get_cmdclass()
cmdclass['build_ext'] = build_ext

setup(name='tsne',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Daniel Rodriguez',
      author_email='df.rodriguez@gmail.com',
      url='https://github.com/danielfrg/py_tsne',
      description='TSNE implementations for python',
      license='Apache License Version 2.0, January 2004',
      packages=find_packages(),
      ext_modules=ext_modules,
      install_requires=required
      )
