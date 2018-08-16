FROM python:3.6.6

RUN apt-get update && apt-get install -y \
        cmake \
        libatlas-base-dev \
    && apt-get clean && \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

ADD requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./docker/base/docker-entrypoint.sh /
CMD []
ENTRYPOINT ["/docker-entrypoint.sh"]
