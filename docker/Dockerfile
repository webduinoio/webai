FROM ubuntu:18.04

MAINTAINER Sipeed support@sipeed.com

RUN apt-get update -qq\
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN DEBIAN_FRONTEND=noninteractive \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
        gcc \
        make \
        perl \
        build-essential \
        zip \
        unzip \
        git \
        wget \
        cmake \
        python3 \
        python3-pip \
    && pip3 install -r https://raw.githubusercontent.com/sipeed/MaixPy/master/requirements.txt \
    && wget https://github.com/kendryte/kendryte-gnu-toolchain/releases/download/v8.2.0-20190409/kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.xz \
    && tar -Jxf kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.xz -C /opt \
    && rm -f kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.xz \
    && mkdir /maixpy \
    && echo "setup complete, now clean" \
    && DEBIAN_FRONTEND=noninteractive apt-get autoremove -y --purge \
    && DEBIAN_FRONTEND=noninteractive apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp \
    && ln -s /usr/bin/cmake /usr/local/bin/cmake \
    && alias python=python3 \
    && echo "build complete"