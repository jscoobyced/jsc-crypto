#!/bin/bash

docker pull jscdroiddev/jsc-crypto:latest
docker run -d -p 8888:8888 --mount type=bind,source="$(pwd)"/data,target=/opt/jsc_crypto/data --name jsc_crypto --restart unless-stopped jscdroiddev/jsc-crypto:latest