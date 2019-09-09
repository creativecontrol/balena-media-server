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

echo "I recommend sharing your control computer SSH key with all of the \
Raspberry Pis on the network to make things easier"
echo "ssh-copy-id pi@<rpi hostname>"
echo ""

echo "please edit the /boot/cmdline.txt by adding consoleblank=10"
echo "this will ensure the console is black if the video is stopped"
echo "you'll need to reboot afterwards"
echo "sudo nano /boot/cmdline.txt"
