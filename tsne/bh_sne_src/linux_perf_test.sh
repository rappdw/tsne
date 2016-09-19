#!/usr/bin/env bash

LOG=/dev/stdout
/usr/bin/time -f '%e %M' -o $LOG ./bh_tsne
