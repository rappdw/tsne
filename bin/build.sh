#!/usr/bin/env bash

bin/build-linux.sh
bin/build-osx.sh

rm dist/*linux_x86*.whl
mv wheelhouse/*.whl dist/
rm -rf wheelhouse