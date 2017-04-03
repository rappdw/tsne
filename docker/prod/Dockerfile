FROM python:3.6.1

RUN apt-get update && apt-get install -y \
        libatlas-base-dev \
    && apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

#####
# End of Base
#####


WORKDIR /tsne

ADD dist .
#RUN pip install --no-index --find-links=/tsne tsne
