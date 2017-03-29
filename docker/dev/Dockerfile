FROM python:3.6.1

RUN apt-get update && apt-get install -y \
        libatlas-base-dev \
    && apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

WORKDIR /tsne
ADD requirements.txt .

RUN pip install -r /tsne/requirements.txt
# used for test/demo
RUN pip install scikit-learn matplotlib

ENTRYPOINT /usr/local/bin/pip install -e /tsne && /bin/bash


