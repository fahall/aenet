#!/bin/bash
sudo nvidia-docker build -t $USER/aenet:CUDA8-py27 .
sudo nvidia-docker run --rm -ti --volume=$(pwd):/aenet:rw --volume=/mnt/data/alex/data:/data:rw --workdir=/aenet --ipc=host $USER/aenet:CUDA8-py27 /bin/bash
