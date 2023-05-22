#!/bin/bash

python3 ./visualize.py
cp ./result.png /usr/share/nginx/html/

nginx -g "daemon off;"