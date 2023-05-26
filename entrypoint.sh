#!/bin/bash

mkdir -p ./static/
python3 ./visualize.py
chmod 600 ./result.png
mv ./result.png ./static/

export FLASK_APP=app
export FLASK_RUN_HOST=0.0.0.0

python3 -m flask run
