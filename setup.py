import sys

from os import path
from setuptools import setup, Extension, find_packages

import versioneer


if __name__ == "__main__":

    args = sys.argv[1:]

    run_build = True
    other_commands = ['egg_info', 'install_egg_info', 'rotate']
    for command in other_commands:
        if command in args:
            run_build = False

    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    cmdclass = versioneer.get_cmdclass()

    metadata = dict(
        name='tsne-mp',
        version=versioneer.get_version(),
        cmdclass=cmdclass,
        author='Daniel Rapp',
        author_email='rappdw@gmail.com',
        url='https://github.com/rappdw/tsne.git',
        description='High Performance TSNE implementations for python',
        long_description=long_description,
        long_description_content_type="text/markdown",

        license='Apache License Version 2.0, January 2004',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Visualization',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        packages=find_packages(),
        scripts=['tsne/bh_sne_src/bhtsne.py'],
        install_requires=[
            'numpy',
            'scipy'
        ],
        setup_requires=[
            # Setuptools 18.0 properly handles Cython extensions.
            'setuptools>=18.0',
            'cython',
            'numpy'
        ]
    )

    if run_build:
        import numpy
        from Cython.Build import cythonize

        if sys.platform == 'darwin':
            # OS X
            library_dirs = []
            compile_args = ['-Xpreprocessor', '-fopenmp', '-lomp' '-ffast-math', '-flto']
            link_args = ['-Wl,-framework', '-Wl,Accelerate', '-lomp']
        else:
            # LINUX
            library_dirs = ['/usr/local/lib', '/usr/lib64/atlas']
            compile_args = ['-O3', '-flto', '-ffast-math', '-fopenmp']
            # compile_args = ['-msse2', '-fPIC', '-w', '-ffast-math', '-O2', '-fopenmp', '-flto']  # + ['-DTSNE3D']
            link_args = compile_args + ['-lgomp']

        ext_modules = [Extension(name='tsne.bh_sne',
                                 sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp', 'tsne/bh_sne.pyx'],
                                 include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                                 library_dirs=library_dirs,
                                 extra_compile_args=compile_args,
                                 extra_link_args=link_args,
                                 language='c++'),

                       Extension(name='tsne.bh_sne_3d',
                                 sources=['tsne/bh_sne_src/sptree.cpp', 'tsne/bh_sne_src/tsne.cpp',
                                          'tsne/bh_sne_3d.pyx'],
                                 include_dirs=[numpy.get_include(), 'tsne/bh_sne_src/'],
                                 library_dirs=library_dirs,
                                 extra_compile_args=compile_args + ['-DTSNE3D'],
                                 extra_link_args=link_args,
                                 language='c++')]

        metadata['ext_modules'] = cythonize(ext_modules)
    else:
        # Don't import numpy here - non-build actions are required to succeed
        # without Numpy for example when pip is used to install Scipy when
        # Numpy is not yet present in the system.
        metadata['name'] = 'tsne-mp'

    setup(**metadata)

