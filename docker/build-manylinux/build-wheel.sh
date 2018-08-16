#!/usr/bin/env bash

BASE_PATH=$PATH
PYTHON_PATH="/opt/python/"$1"-"$1"m/bin"
export PATH=$PYTHON_PATH:$PATH

pip install -q numpy cython

if [ -d "dist" ]; then
    mv dist dist.tmp.$1
fi

python setup.py -qqq bdist_wheel
auditwheel repair dist/*.whl

if [ -d "dist.tmp.$1" ]; then
    mv dist.tmp.$1/* dist/
    rm -rf dist.tmp.$1
fi

rm -rf *.pyc *.so build/ bh_sne.cpp bh_sne_3d.cpp
rm -rf tsne/*.pyc tsne/*.so tsne/bh_sne.cpp tsne/bh_sne_3d.cpp
