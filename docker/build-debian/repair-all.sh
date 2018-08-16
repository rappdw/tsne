#!/usr/bin/env bash
set -x

cd /workdir

for wheel in ./dist/*.whl; do
    auditwheel repair $wheel
done

