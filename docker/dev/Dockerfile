FROM python:3.6.1

RUN apt-get update && apt-get install -y \
        cmake \
        libatlas-base-dev \
    && apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

#####
# End of Base
#####


# used for test/demo
RUN pip install scikit-learn matplotlib

WORKDIR /tsne
ADD . /tsne

ENTRYPOINT /usr/local/bin/pip install -e /tsne && /bin/bash


