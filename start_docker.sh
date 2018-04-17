#!/bin/bash

docker load -i docker_image.tar
docker run -dt -v "$PWD/":/var/www/html/lianshanguankong/ \
    -p 80:80 \
    c82e8d1e6efb \
    /var/www/html/lianshanguankong/start_website.sh