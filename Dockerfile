FROM nvidia/cuda:11.4.3-base-ubuntu20.04

RUN apt-get update && \
    apt-get install -y \
      wget \
      build-essential \
      zlib1g-dev \
      libssl-dev \
      libffi-dev \
      libbz2-dev \
      libreadline-dev \
      libsqlite3-dev \
      libncurses5-dev \
      libgdbm-dev \
      liblzma-dev && \
    wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz && \
    tar -xzf Python-3.10.12.tgz && \
    cd Python-3.10.12 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.10.12 Python-3.10.12.tgz

RUN python3.10 -m ensurepip && \
    python3.10 -m pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.10 -m pip install -r requirements.txt

COPY . /app

CMD ["python3.10", "app.py"]
