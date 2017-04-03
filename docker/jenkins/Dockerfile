FROM python:3.6.1

RUN apt-get update && apt-get install -y \
        libatlas-base-dev \
    && apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

#####
# End of Base
#####

# dependencies required to run setup.py
RUN pip install Cython numpy wheel

WORKDIR /tsne
ADD . /tsne

VOLUME /tsne/dist /tsne/.git

# the intent here is to run this container as follows:
#   docker run --rm -it -v $PWD/dist:/tsne/dist -v $PWD/.git:/tsne/.git:ro tsne-jenkins /bin/bash
#
# within the container you can run commands like `python setup.py bdist_wheel` etc.
#
# The mount of dist is present to allow unloading of generated distributions
# The mount of .git is to allow versions to be resolved correctly