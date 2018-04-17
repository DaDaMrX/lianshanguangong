#!/bin/bash

/etc/init.d/nginx start
/usr/local/bin/uwsgi --chdir=/var/www/html/lianshanguankong/register_system \
    --module=register_system.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=register_system.settings \
    --socket=127.0.0.1:49152 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum \
    --master \
    --pidfile=/tmp/project-master.pid \
    --threads 8 
#    --daemonize=/var/log/uwsgi/register_system.log