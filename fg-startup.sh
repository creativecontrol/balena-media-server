#!/usr/bin/env bash
# This will start up the omx player process like this:

source ./fg-player/bin/activate

# Start the OSC server with the computer's hostname so others can get to it on
# the network.
python fg-omx-player.py --ip="$HOSTNAME.local"
