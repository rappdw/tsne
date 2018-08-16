#!/usr/bin/env bash

set -ex

build_wheel() {
    pipenv --python $1
    pipenv install -r requirements.txt
    pipenv run python setup.py bdist_wheel
    pipenv --rm
}

build_wheel 3.5
build_wheel 3.6
build_wheel 3.7
