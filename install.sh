#!/usr/bin/env bash

# Make sure OMXPlayer is installed
apt install omxplayer

# make sure prerequisites for OMXPlayer Wrapper are installed
apt-get update && apt install -y libdbus-1{-3,-dev}

apt install python3-venv
apt install python3-pip

# setup venv
python3 -m venv fg-player

source ./fg-player/bin/activate

# install requirements
pip install -r requirements.txt

deactivate
