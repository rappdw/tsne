#!/usr/bin/env bash

build_wheel() {
    source activate $1

    python setup.py bdist_wheel

    source deactivate
}

build_wheel py35
build_wheel py36
build_wheel py37