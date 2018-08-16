FROM quay.io/pypa/manylinux1_x86_64

RUN yum install -y \
        atlas-devel \
        blas-devel

WORKDIR /workdir

ADD docker/build-manylinux/build-wheel.sh /

ENTRYPOINT ["/build-wheel.sh"]
CMD ["cp36"]
