FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt-get update && apt-get install -y rsync htop git openssh-server
RUN apt-get install -y build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
RUN apt-get install -y wget software-properties-common

# ffmpeg
RUN add-apt-repository -y ppa:jonathonf/ffmpeg-3
RUN apt install -y ffmpeg

# Python Basics
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install tqdm moviepy requests pydub

# Lasagne
RUN pip install -r https://raw.githubusercontent.com/Lasagne/Lasagne/master/requirements.txt
RUN pip install https://github.com/Lasagne/Lasagne/archive/master.zip



# Run AENet downloads

VOLUME ["/data"]
ADD . /aenet
ENV AENET_DATA_DIR /data/aenet
RUN /aenet/bin/download.sh
# RUN python /aenet/setup.py install

