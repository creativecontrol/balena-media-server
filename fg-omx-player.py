#!/usr/bin/env python3

"""
Fasting Girls OMX Player
Uses OMXPlayer, OMXPlayer Wrapper, and OSC to create a remotely controllable
video player.
"""

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse
import math
from typing import List, Any

"""
Start the Player with a black image to initialize the OMXPlayer instance.
starting with --win to activate the alpha because of an issue with the
current OMX implementation. https://github.com/popcornmix/omxplayer/issues/712 
"""
player = OMXPlayer("images/1920x1080-black-solid-color-background.jpg", args='--win 0,0,1920,1080')

def video_things():
  global player
  VIDEO_PATH = Path("movies/SynthOnASunday_no1_excerpt.mp4")
  BLANK = 24

  player = OMXPlayer(VIDEO_PATH)

"""
The Load handler allows for loading a video file with an optional starting
pause state (<address> <file path> <pause=False>)
"""
def load_handler(addr, *args: List[Any]) -> None:
  global player
  print(args)
  if len(args) > 1:
      player.load(args[0], args[1])
  else:
      player.load(args[0])

def play_handler(addr):
  global player
  player.play()

def pause_handler(addr):
  global player
  player.pause()

def stop_handler(addr):
  global player
  player.stop()

def mute_handler(addr):
  global player
  player.mute()

def unmute_handler(addr):
  global player
  player.unmute()

def action_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_alpha(args[0])

def alpha_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_alpha(args[0])

def rate_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_rate(args[0])

def seek_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.seek(args[0])

def position_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_position(args[0])

def video_pos_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_video_pos(args[0], args[1], args[2], args[3])

def video_crop_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_video_crop(args[0], args[1], args[2], args[3])

def aspect_handler(addr, *args: List[Any]) -> None:
    global player
    print(args)
    player.set_aspect_mode(args[0])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/load", load_handler)
  dispatcher.map("/play", play_handler)
  dispatcher.map("/pause", pause_handler)
  dispatcher.map("/stop", stop_handler)
  dispatcher.map("/mute", mute_handler)
  dispatcher.map("/unmute", unmute_handler)
  dispatcher.map("/alpha", alpha_handler)
  dispatcher.map("/action", action_handler)
  dispatcher.map("/rate", rate_handler)
  dispatcher.map("/seek", seek_handler)
  dispatcher.map("/position", position_handler)
  dispatcher.map("/video_pos", video_pos_handler)
  dispatcher.map("/video_crop", video_crop_handler)
  dispatcher.map("/aspect", aspect_handler)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
