#!/usr/bin/env bash

build-image build-manylinux
run-image build-manylinux -c cp35
run-image build-manylinux -c cp36
run-image build-manylinux -c cp37

# for debian specific build
# build-image build-debian
# run-image build-debian
# currently unable to create a manylinux wheel from the debian specific build, due to utilization of new APIs
# docker run --rm -it -v $PWD:/workdir quay.io/pypa/manylinux1_x86_64 /workdir/docker/build-debian/repair-all.sh