#!/usr/bin/env bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ..

if [ -z "$VIRTUAL_ENV" ]; then
    . activate
fi

twine upload -r pypi dist/*
