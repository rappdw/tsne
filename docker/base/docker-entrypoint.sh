#!/usr/bin/env bash

WORKDIR=${WORKDIR:-"/workdir"}

# install the module mounted in $WORKDIR
if [ -e $WORKDIR/setup.py ]; then
    pip install -e $WORKDIR
fi

exec "$@"
