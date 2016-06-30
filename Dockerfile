FROM ubuntu:14.04
RUN apt-get update && apt-get install -y \
        curl \
        autoconf \
        automake \
        libtool \
        make \
        unzip \
        build-essential \
        g++ \
        git \
        python-dev \
        capnproto \
        vim \
        protobuf-compiler \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /protobuf \
    && cd /protobuf \
    &&  curl -o protobufs.zip -L https://github.com/google/protobuf/releases/download/v3.0.0-beta-3/protoc-3.0.0-beta-3-linux-x86_64.zip \
    && unzip protobufs.zip -d protobuf_dir \
    && cd protobuf_dir \
    && export PATH=$(pwd):$PATH

# Install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
        python get-pip.py && \
        rm get-pip.py

RUN pip --no-cache-dir install \
        cython \
        setuptools \
        pycapnp

RUN git clone https://github.com/richardliaw/test_proto/ /root/examples

WORKDIR "/root"
CMD ["/bin/bash"]
